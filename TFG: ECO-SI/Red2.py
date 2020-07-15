#!/usr/bin/env python
from pandas_datareader import data
import tensorflow as tf
import numpy as np
import shutil
from tensorflow.examples.tutorials.mnist import input_data
import os
from PIL import Image
import time
import os
from scipy.misc import imread, imresize

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#Parametros
tiempo_inicio = time.time()
tam_lote = 3
num_clases = 2
epoch_entrenamiento = 49  #numero de epoch

def inic_pesos(forma):
 var = tf.Variable(tf.random_normal(forma, stddev=0.01))
 return var
 
def modelo(imagen, w1, w4, w_salida, prob_conv, prob_oc):
 conv1 = tf.nn.conv2d(imagen, w1, strides=[1, 1, 1, 1], padding='SAME')
 conv1_a = tf.nn.relu(conv1)
 conv1 = tf.nn.max_pool(conv1_a, ksize=[1, 2, 2, 1] ,strides=[1, 2, 2, 1],  padding='SAME')
 conv1 = tf.nn.dropout(conv1, prob_conv)
 
 capa_cc = tf.reshape(conv1, [-1, w4.get_shape().as_list()[0]])
 capa_cc = tf.nn.dropout(capa_cc, prob_conv)
 
 capa_s = tf.nn.relu( tf.matmul(capa_cc, w4) + bias)
 capa_s = tf.nn.dropout(capa_s, prob_oc, name="dropout_2")


 resultado = tf.matmul(capa_s, w_salida, name="MatMul_1") + bias2

 return resultado

# Ruta del dataset
cwd = os.getcwd()
ruta_dataset = cwd + "/data/custom_data2.npz"
l = np.load(ruta_dataset)

# Cargado dataset
trainimg = l['trainimg']
train = l['train_2']
validationimg = l['validationimg']
validation = l['validation_2']
testimg = l['testimg']
test = l['test_2']
imgsize = l['imgsize']
use_gray = l['use_gray']

ntrain = trainimg.shape[0]

#Reshape imagenes
img_entrenamiento = trainimg.reshape(-1, 800, 400, 3) # 28x28x1 input img
etq_entrenamiento = train
img_val = validationimg.reshape(-1, 800, 400, 3) # 28x28x1 input img
etq_val = validation
img_test = testimg.reshape(-1, 800, 400, 3) # 28x28x1 input img
etq_test = test

#Placeholders para entrenamiento/validacion/prueba
imagen = tf.placeholder("float", [None, 800, 400, 3])
etiqueta = tf.placeholder("float32", [None, num_clases])

prob_conv = tf.placeholder("float")
prob_oc = tf.placeholder("float")

#Pesos y bias 
w = inic_pesos([7, 7, 3, 12 ])
w4 = inic_pesos([(int)(12*(800/2)*(400/2)), 32]) #(400/2)*(200/2)
w_salida = inic_pesos([32, num_clases])	
bias = tf.Variable(tf.random_normal([32]))
bias2 = tf.Variable(tf.random_normal([num_clases]))


#Calculos metricas
modelo = modelo(imagen, w, w4, w_salida, prob_conv, prob_oc)
y = tf.nn.softmax_cross_entropy_with_logits_v2(logits=modelo ,labels=etiqueta)
coste= tf.reduce_mean(y)
opt = tf.train.AdamOptimizer(learning_rate=0.00005).minimize(coste)
probabilidades = tf.nn.softmax(modelo)
predic = tf.argmax(modelo, 1)
correctas = tf.equal(predic, tf.argmax(etiqueta,1)) # Count corrects
precision = tf.reduce_mean(tf.cast(correctas, tf.float32)) # Accuracy


#Metricas a seguir en Tensorboard
tf_coste_ph = tf.placeholder(tf.float32,shape=None,name='coste_summary')
tf_coste_summary = tf.summary.scalar('coste', tf_coste_ph)

tf_precision_ph = tf.placeholder(tf.float32,shape=None, name='precision_summary')
tf_precision_summary = tf.summary.scalar('precision', tf_precision_ph)

summaries = tf.summary.merge([tf_coste_summary,tf_precision_summary])
summaries2 = tf.summary.merge([tf_coste_summary,tf_precision_summary])

# Variables entrenamiento
o_id= 0
id    = tam_lote-1 
num_lotes = int(round(ntrain/tam_lote))

# Inicializacion sesion, grafo y writers Tensorboard
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
summ_writer = tf.summary.FileWriter(os.path.join('summaries','first'), sess.graph)
summ_writer2 = tf.summary.FileWriter(os.path.join('summaries','second'), sess.graph)
write_op = tf.summary.merge_all()

# Inicio entrenamiento
for epoch in range(epoch_entrenamiento):
    coste_medio = 0
    precision_media = 0
    print ("Epoch: %03d/%03d" % (epoch+1, epoch_entrenamiento))
	
    # TRAINING
    for i in range(num_lotes):
     if i != 0:
      o_id=id+1
      id=id+tam_lote	 
     lote_x = img_entrenamiento[o_id:id, :]
     lote_y = etq_entrenamiento[o_id:id, :]       

    # Ejecucion entrenamiento
     sess.run(opt, feed_dict={imagen: lote_x, etiqueta: lote_y, prob_conv: 0.8, prob_oc: 0.5})
	 
    # Calculo coste y precision
     c,e_prec = sess.run([coste,precision], feed_dict={imagen: lote_x, etiqueta: lote_y, prob_conv:1.0, prob_oc: 1.0})
     coste_medio+= c
     precision_media+= e_prec
    precision_media = precision_media/num_lotes
    coste_medio = coste_medio/num_lotes
    print (" Precision entrenamiento: %.3f - Coste entrenamiento: %.3f" % (precision_media,coste_medio))
	
    if epoch<epoch_entrenamiento:
      o_id= 0
      id    = tam_lote-1
    # VALIDATION
    val_prec,c2 = sess.run([precision,coste], feed_dict={imagen: img_val, etiqueta: etq_val, prob_conv: 1.0, prob_oc: 1.0})
    print (" Precision validacion: %.3f - Coste validacion: %.3f " % (val_prec,c2))

    train = sess.run(summaries, feed_dict={tf_coste_ph:coste_medio, tf_precision_ph: precision_media})
    summ_writer.add_summary(train,epoch)
    summ_writer.flush()
	
    val = sess.run(summaries2, feed_dict={tf_coste_ph:c2, tf_precision_ph: val_prec})
    summ_writer2.add_summary(val, epoch)
    summ_writer2.flush()
	
# TESTING
test_prec,c3 = sess.run([precision,coste], feed_dict={imagen: img_test, etiqueta: etq_test, prob_conv: 1.0, prob_oc: 1.0})
print (" Precision pruebas: %.3f - Coste pruebas: %.3f " % (val_prec,c2))

# Guardado modelo
print('\nGuardando...')
ruta = os.path.join(cwd, 'Redes/2')
shutil.rmtree(ruta, ignore_errors=True)
inputs_dict = {
	"imagenes_ph": imagen,
	"etiqueta_ph": etiqueta
	}
outputs_dict = {
    "logits": modelo,
    "probabilidades": probabilidades
    }
tf.saved_model.simple_save(
                sess, ruta, inputs_dict, outputs_dict
            )
print('Ok. Guardado.')
sess.close()
print("--- %s segundos ---" % (time.time() - tiempo_inicio))


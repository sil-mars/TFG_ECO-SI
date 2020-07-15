
import numpy as np
import os
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
import glob
import tensorflow as tf 


print ("Codificando el dataset...") 
cwd = os.getcwd()
print ("La carpeta actual es %s" % (cwd) )

# Training set folder 
paths = {"/dataset/imagenes"}
# The reshape size
imgsize = [800, 400]
# Grayscale
use_gray = 0
# Save name
data_name = "custom_data"

print ("Las imagenes deberian estar en")
for i, path in enumerate(paths):
    print (" [%d/%d] %s/%s" % (i, len(paths), cwd, path)) 

print ("El dataset se guardara en %s" 
       % (cwd + '/data/'))
	   
	   
def rgb2gray(rgb):
    if len(rgb.shape) is 3:
        return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    else:
        # print ("Current Image if GRAY!")
        return rgb
		
nclass = len(paths)
valid_exts = [".jpg",".gif",".png",".tga", ".jpeg"]
imgcnt     = 0
for i, relpath in zip(range(nclass), paths):
    path = cwd + "/" + relpath
    flist = os.listdir(path)
    for f in flist:
        if os.path.splitext(f)[1].lower() not in valid_exts:
            continue
        fullpath = os.path.join(path, f)
        currimg  = imread(fullpath)
        # Convert to grayscale  
        if use_gray:
            grayimg  = rgb2gray(currimg)
        else:
            grayimg  = currimg
        # Reshape
        graysmall = imresize(grayimg, [imgsize[0], imgsize[1]])/255.
        grayvec   = np.reshape(graysmall, (1, -1))
        # Save 
        if "latabolsacolillabrickplastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[1,0]]
            label_colilla = [[1,0]]
        elif "bolsacolillabrickplastico" in f:
            label_lata = [[0,1]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[1,0]]
            label_colilla = [[1,0]]
        elif "latacolillabrickplastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "latabolsabrickplastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[1,0]]
            label_colilla = [[0,1]]
        elif "latabolsacolillaplastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[0,1]]
            label_bolsa = [[1,0]]
            label_colilla = [[1,0]]
        elif "latabolsacolillabrick" in f:
            label_lata = [[1,0]]
            label_plastico = [[0,1]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "colillaplasticobrick" in f:
            label_lata = [[0,1]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "bolsabrickplastico" in f:
            label_lata = [[0,1]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[1,0]]
            label_colilla = [[0,1]]
        elif "bolsacolillaplastico" in f:
            label_lata = [[0,1]]
            label_plastico = [[1,0]]
            label_brick = [[0,1]]
            label_bolsa = [[1,0]]
            label_colilla = [[1,0]]
        elif "bolsacolillabrick" in f:
            label_lata = [[0,1]]
            label_plastico = [[0,1]]
            label_brick = [[1,0]]
            label_bolsa = [[1,0]]
            label_colilla = [[1,0]]
        elif "latacolillabrick" in f:
            label_lata = [[1,0]]
            label_plastico = [[0,1]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "latabrickplastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[0,1]]
        elif "latabolsacolilla" in f:
            label_lata = [[1,0]]
            label_plastico = [[0,1]]
            label_brick = [[0,1]]
            label_bolsa = [[1,0]]
            label_colilla = [[1,0]]
        elif "latacolillaplastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[0,1]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "latabolsaplastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[0,1]]
            label_bolsa = [[1,0]]
            label_colilla = [[0,1]]
        elif "latabolsabrick" in f:
            label_lata = [[1,0]]
            label_plastico = [[0,1]]
            label_brick = [[1,0]]
            label_bolsa = [[1,0]]
            label_colilla = [[0,1]]	
        elif "plasticobrick" in f:
            label_lata = [[0,1]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[0,1]]
        elif "colillaplastico" in f:
            label_lata = [[0,1]]
            label_plastico = [[1,0]]
            label_brick = [[0,1]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "colillabrick" in f:
            label_lata = [[0,1]]
            label_plastico = [[0,1]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "bolsaplastico" in f:
            label_lata = [[0,1]]
            label_plastico = [[1,0]]
            label_brick = [[0,1]]
            label_bolsa = [[1,0]]
            label_colilla = [[0,1]]
        elif "bolsabrick" in f:
            label_lata = [[0,1]]
            label_plastico = [[0,1]]
            label_brick = [[1,0]]
            label_bolsa = [[1,0]]
            label_colilla = [[0,1]]
        elif "bolsacolilla" in f:
            label_lata = [[0,1]]
            label_plastico = [[0,1]]
            label_brick = [[0,1]]
            label_bolsa = [[1,0]]
            label_colilla = [[1,0]]
        elif "lataplastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[0,1]]
            label_bolsa = [[0,1]]
            label_colilla = [[0,1]]
        elif "latabrick" in f:
            label_lata = [[1,0]]
            label_plastico = [[0,1]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[0,1]]
        elif "latacolilla" in f:
            label_lata = [[1,0]]
            label_plastico = [[0,1]]
            label_brick = [[0,1]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "latabolsa" in f:
            label_lata = [[1,0]]
            label_plastico = [[0,1]]
            label_brick = [[0,1]]
            label_bolsa = [[1,0]]
            label_colilla = [[0,1]]
        elif "lata" in f:
            label_lata = [[1,0]]
            label_plastico = [[0,1]]
            label_brick = [[0,1]]
            label_bolsa = [[0,1]]
            label_colilla = [[0,1]]
        elif "brick" in f:
            label_lata = [[0,1]]
            label_plastico = [[0,1]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[0,1]]
        elif "colilla" in f:
            label_lata = [[0,1]]
            label_plastico = [[0,1]]
            label_brick = [[0,1]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]
        elif "bolsa" in f:
            label_lata = [[0,1]]
            label_plastico = [[0,1]]
            label_brick = [[0,1]]
            label_bolsa = [[1,0]]
            label_colilla = [[0,1]]
        elif "plastico" in f:
            label_lata = [[1,0]]
            label_plastico = [[1,0]]
            label_brick = [[1,0]]
            label_bolsa = [[0,1]]
            label_colilla = [[1,0]]		
        if imgcnt is 0:
            totalimg   = grayvec
            total_1 = label_lata
            total_2 = label_plastico
            total_3 = label_brick
            total_4 = label_bolsa
            total_5 = label_colilla
        else:
            totalimg   = np.concatenate((totalimg, grayvec), axis=0)
            total_1 = np.concatenate((total_1,label_lata), axis=0)
            total_2 = np.concatenate((total_2,label_plastico), axis=0)
            total_3 = np.concatenate((total_3,label_brick), axis=0)
            total_4 = np.concatenate((total_4,label_bolsa), axis=0)
            total_5 = np.concatenate((total_5,label_colilla), axis=0)
        imgcnt    = imgcnt + 1

		
print ("Total: %d imagenes cargadas." % (imgcnt))

def print_shape(string, x):
    print ("Shape de '%s' es %s" % (string, x.shape,))

total_1 = total_1.astype(int, copy=False)
total_2 = total_2.astype(int, copy=False)
total_3 = total_3.astype(int, copy=False)
total_4 = total_4.astype(int, copy=False)
total_5 = total_5.astype(int, copy=False)

#---RANDOMIZAR ORDEN DATASETS---	
randidx    = np.random.randint(imgcnt, size=imgcnt)
trainidx   = randidx[0:int(3*imgcnt/5)]
validationidx    = randidx[int(3*imgcnt/5) :int(4*imgcnt/5)]
testidx = randidx[int(4*imgcnt/5) : imgcnt]

trainimg   = totalimg[trainidx , :]
train_1 = total_1[trainidx, :]
train_2 = total_2[trainidx, :]
train_3 = total_3[trainidx, :]
train_4 = total_4[trainidx, :]
train_5 = total_5[trainidx, :]

validationimg   = totalimg[validationidx , :]
validation_1 = total_1[validationidx, :]
validation_2 = total_2[validationidx, :]
validation_3 = total_3[validationidx, :]
validation_4 = total_4[validationidx, :]
validation_5 = total_5[validationidx, :]

testimg    = totalimg[testidx, :]
test_1  = total_1[testidx, :]
test_2  = total_2[testidx, :]
test_3  = total_3[testidx, :]
test_4  = total_4[testidx, :]
test_5  = total_5[testidx, :]


savepath_1 = cwd + "/data/" + data_name + "1.npz"
savepath_2 = cwd + "/data/" + data_name + "2.npz"
savepath_3 = cwd + "/data/" + data_name + "3.npz"
savepath_4 = cwd + "/data/" + data_name + "4.npz"
savepath_5 = cwd + "/data/" + data_name + "5.npz"



np.savez(savepath_1, trainimg=trainimg, validationimg = validationimg, testimg=testimg
         , train_1 = train_1, validation_1 = validation_1, test_1 = test_1, imgsize=imgsize, use_gray=use_gray)
		 
np.savez(savepath_2, trainimg=trainimg, validationimg = validationimg, testimg=testimg
         , train_2 = train_2, validation_2 = validation_2, test_2 = test_2, imgsize=imgsize, use_gray=use_gray)
		 
np.savez(savepath_3, trainimg=trainimg, validationimg = validationimg, testimg=testimg
         , train_3 = train_3, validation_3 = validation_3, test_3 = test_3, imgsize=imgsize, use_gray=use_gray)
		 
np.savez(savepath_4, trainimg=trainimg, validationimg = validationimg, testimg=testimg
         , train_4 = train_4, validation_4 = validation_4, test_4 = test_4, imgsize=imgsize, use_gray=use_gray)
		 
np.savez(savepath_5, trainimg=trainimg, validationimg = validationimg, testimg=testimg
         , train_5 = train_5, validation_5 = validation_5, test_5 = test_5, imgsize=imgsize, use_gray=use_gray)


print ("%d imagenes de entrenamiento guardadas" % (trainimg.shape[0]))
print ("%d imagenes de validacion guardadas" % (validationimg.shape[0]))
print ("%d imagenes de prueba guardadas" % (testimg.shape[0]))
print ("Guardadas en " +cwd + '/data/')


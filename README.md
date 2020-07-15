# TFG: ECO-SI.
## Description/Descripción.
Intelligent system able to classify 5 different types of waste. For the image classification Covolutional Neural Networks(CNNs) are used. They are implemented modifying MNIST number recognition base code and using the idea of one vs all to deal with the multiclass problem.
The 5 types of waste identified are: cans, plastic bags, cigarettes, some plastic objects (like spoons or glasses) and tetrabriks.

Sistema inteligente capaz de clasificar 5 tipos distintos de desperdicios. Para la clasificación de imágenes se utilizan Redes Neuronales Convolucionales(CNN). Para su implementación se ha tomado como base el código del MNIST de clasificación de números y se ha utilizado la idea de uno contra todos para dar solución al problema de la multiclase.
Los cinco tipos de desperdicios identificados son: latas, bolsas de plástico, colillas, plásticos (como vasos o cucharas de plástico) y bricks.

## Instructions/Instrucciones.
Tensorflow and Python must be installed. Using GPU for training is recommended. Dataset is expected to be encoded in .npz
  1. Execute each "Red.py" separately generating the different trained networks. Careful with the dataset path!
  2. Place the trained networks in ECO-SI App/Redes/ (or the selected route if you edited Predictor.java in ECO-SI App/src/ ).
  3. Execute Main.java in ECO-SI App. This small program will let you upload a photo to classify and will return the prediction by putting together the results of each network.

Se deben tener instalados Tensorflow y Python. Se recomienda utilizar GPU para el entrenamiento. Se espera que el dataset este codificado en .npz.
  1. Ejecutar cada "Red.py" de forma separada y generando las distintas redes ya entrenadas. ¡Cuidado con la ruta del dataset!
  2. Mover las redes entrenadas a ECO-SI App/Redes/ (o la ruta seleccionada si has editado Predictor.java en ECO-SI App/src/ ).
  3. Ejecutar Main.java en ECO-SI App. Este pequeño programa te permitirá subir una foto y clasificarla devolviendo la predicción al juntar los resultados de cada red.

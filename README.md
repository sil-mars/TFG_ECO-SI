# TFG: ECO-SI.
## Description
Intelligent system able to classify 5 different types of waste. For the image classification Covolutional Neural Networks(CNNs) are used. They are implemented modifying MNIST number recognition base code and using the idea of one vs all to deal with the multiclass problem.
The 5 types of waste identified are: cans, plastic bags, cigarettes, some plastic objects (like spoons or glasses) and tetrabriks.

## Instructions
Tensorflow and Python must be installed. Using GPU for training is recommended. 
  1. Use datasetgen.py to encode the dataset. It is recommended to check the path of the images.
  2. Execute each "Red.py" separately generating the different trained networks. Careful with the dataset path!
  3. Place the trained networks in ECO-SI App/Redes/ (or the selected route if you edited Predictor.java in ECO-SI App/src/
  4. Execute Main.java in ECO-SI App. This small program will let you upload a photo to classify and will return the prediction by putting together the results of each network.

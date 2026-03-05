Fashion MNIST CNN Image Classifier (PyTorch)
Overview

This project builds a Convolutional Neural Network (CNN) using PyTorch to classify images from the FashionMNIST dataset. The model learns visual patterns from grayscale images of clothing items and predicts the category of each image.

The project demonstrates the complete deep learning workflow:

Building a neural network model

Training the model on image data

Saving the trained model

Running inference on test data

Exporting predictions to a CSV file

The goal is to showcase a deep learning image classification pipeline using Python and PyTorch.

Dataset

This project uses the FashionMNIST dataset, a widely used dataset for machine learning and computer vision tasks.

Dataset characteristics:

70,000 images total

60,000 training images

10,000 test images

Image size: 28 × 28 pixels

Grayscale images

10 clothing categories

The dataset is automatically downloaded when the training script runs.

Clothing Categories
Label	Category
0	T-shirt / top
1	Trouser
2	Pullover
3	Dress
4	Coat
5	Sandal
6	Shirt
7	Sneaker
8	Bag
9	Ankle boot
Model Architecture

The model used in this project is a Convolutional Neural Network (CNN) designed for image classification.

CNNs are commonly used in computer vision because they can automatically detect important visual features such as edges, shapes, and textures.

Model Structure
Input Image (28x28)

↓
Convolution Layer
↓
ReLU Activation
↓
Max Pooling

↓
Convolution Layer
↓
ReLU Activation
↓
Max Pooling

↓
Flatten

↓
Fully Connected Layer

↓
Output Layer (10 classes)

The output layer produces a probability score for each clothing category.

Project Workflow

The project consists of two main stages: training the model and generating predictions.

1. Training the Model

The training process is handled by the train.py script.

The script performs the following steps:

Downloads the FashionMNIST dataset

Loads the training images

Builds the CNN model

Trains the model on the dataset

Saves the trained model weights

After training completes, the model parameters are saved as:

fashion_cnn.pth

This file contains the learned weights of the neural network.

2. Generating Predictions

Predictions are generated using the predict.py script.

The script performs the following steps:

Loads the trained model

Processes test images

Predicts the clothing category for each image

Saves the predictions to a CSV file

Output file generated:

predictions.csv
Example CSV Output
image_index	predicted_label
0	9
1	0
2	1
3	8

Each number corresponds to a clothing category listed in the dataset table above.

Installation and Dependencies

This project requires several Python libraries for deep learning, dataset management, and data handling.

Install the required libraries using the following command:

python -m pip install torch torchvision pandas numpy
Python Libraries Used
Library	Purpose
torch	Core deep learning framework used to build and train the neural network
torchvision	Provides the FashionMNIST dataset and image transformation tools
pandas	Used to create and export prediction results to CSV
numpy	Provides numerical computation utilities used in machine learning workflows
Library Explanations
PyTorch (torch)

PyTorch is the main deep learning framework used in this project. It provides tools for:

building neural network models

performing tensor operations

training models using gradient descent

saving and loading trained models

Torchvision (torchvision)

Torchvision is a computer vision library built for PyTorch.

In this project it is used to:

automatically download the FashionMNIST dataset

load image data

convert images into tensors suitable for neural networks

Pandas (pandas)

Pandas is used for working with structured data.

In this project it is used to:

organize prediction results

create a dataframe of predictions

export results to predictions.csv

NumPy (numpy)

NumPy provides efficient numerical operations used in scientific computing and machine learning workflows.

It supports fast array operations and is often used alongside PyTorch.

How to Run the Project
Step 1 — Train the Model

Run the training script:

python train.py

This will:

download the dataset

train the neural network

save the trained model

Output generated:

fashion_cnn.pth
Step 2 — Generate Predictions

Run the prediction script:

python predict.py

This will:

load the trained model

generate predictions on test data

export the predictions

Output generated:

predictions.csv
Files Included
File / Folder	Description
model.py	Defines the CNN neural network architecture
train.py	Trains the model using the FashionMNIST dataset
predict.py	Loads the trained model and generates predictions
predictions.csv	CSV file containing predicted labels for test images
fashion_cnn.pth	Saved neural network model weights
data/	Dataset downloaded automatically by torchvision
__pycache__/	Python cache files generated during execution
README.md	Project documentation
Project Objective

The objective of this project is to demonstrate how deep learning models can be used for image classification. By training a convolutional neural network on image data, the model learns patterns that allow it to categorize clothing items automatically.

The workflow highlights the use of PyTorch for model development, training, and inference.

Example Applications

Image classification models like this can be applied to:

E-commerce product categorization

Automated image tagging

Retail inventory systems

Computer vision pipelines

AI-based recommendation systems

# Fashion MNIST CNN Image Classifier (PyTorch)

## Overview

This project builds a **Convolutional Neural Network (CNN)** using **PyTorch** to classify images from the **FashionMNIST dataset**. The model learns visual patterns from grayscale clothing images and predicts the category of each item.

FashionMNIST is a dataset created by **Zalando**, a large European online fashion retailer headquartered in Germany. The dataset was introduced as a more challenging replacement for the traditional MNIST handwritten digit dataset, which had become too simple for modern machine learning algorithms.

The dataset contains **70,000 grayscale images of clothing items**, each belonging to one of **10 fashion categories** such as shirts, trousers, dresses, sneakers, and bags. Each image is **28×28 pixels**, making the dataset lightweight and ideal for experimenting with deep learning models.

In this project, a **Convolutional Neural Network (CNN)** is trained to automatically learn patterns from these images and classify them into the correct clothing category.

The project demonstrates a full deep learning workflow including:

- Building a neural network architecture
- Training a model on image data
- Saving trained model weights
- Running inference on unseen data
- Exporting predictions to a CSV file


This project showcases **deep learning and computer vision using Python and PyTorch**.

---

# Dataset

This project uses the **FashionMNIST dataset**, a widely used dataset for computer vision and machine learning tasks.

Dataset characteristics:

- **70,000 total images**
- **60,000 training images**
- **10,000 test images**
- Image size: **28 × 28 pixels**
- Grayscale images
- **10 clothing categories**


### Clothing Categories

| Label | Category |
|------|---------|
| 0 | T-shirt / top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

## Dataset Download

The FashionMNIST dataset is **not included in this repository**.

When the training script runs, the dataset is automatically downloaded using `torchvision` and stored locally in a `data/` folder.

This prevents the repository from containing large files while keeping the project easy to run.

The dataset will be downloaded automatically when running:


python train.py

# Model Architecture

The model used in this project is a **Convolutional Neural Network (CNN)** designed for image classification.

CNNs are commonly used in computer vision because they can automatically detect visual features such as edges, shapes, and textures.

### Model Structure

```
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
```

The output layer predicts the probability of each clothing category.

---

# Project Workflow

The project consists of two main stages: **training the model** and **generating predictions**.

---

## 1. Training the Model

The training process is handled by **train.py**.

The script performs the following steps:

1. Downloads the FashionMNIST dataset
2. Loads the training images
3. Builds the CNN model
4. Trains the neural network
5. Saves the trained model weights

After training completes, the model parameters are saved as:

```
fashion_cnn.pth
```

This file contains the learned weights of the neural network.

---

## 2. Generating Predictions

Predictions are generated using **predict.py**.

The script performs the following steps:

1. Loads the trained model
2. Processes test images
3. Predicts the clothing category for each image
4. Saves the predictions to a CSV file

Output file generated:

```
predictions.csv
```

### Example CSV Output

| image_index | predicted_label |
|-------------|----------------|
| 0 | 9 |
| 1 | 0 |
| 2 | 1 |
| 3 | 8 |

Each number corresponds to a clothing category listed in the dataset table above.

---

# Installation and Dependencies

Install the required libraries using:

```
python -m pip install torch torchvision pandas numpy
```

---

# Python Libraries Used

| Library | Purpose |
|--------|--------|
| **torch** | Deep learning framework used to build and train the neural network |
| **torchvision** | Provides the FashionMNIST dataset and image utilities |
| **pandas** | Used to organize and export predictions to CSV |
| **numpy** | Provides numerical operations used in machine learning workflows |

---

# Library Explanations

### PyTorch (`torch`)

PyTorch is the main deep learning framework used in this project. It provides tools for:

- building neural networks
- performing tensor operations
- training models using gradient descent
- saving and loading trained models

---

### Torchvision (`torchvision`)

Torchvision provides datasets and utilities for computer vision tasks.

In this project it is used to:

- automatically download the **FashionMNIST dataset**
- load image data
- convert images into tensors

---

### Pandas (`pandas`)

Pandas is used to handle structured data.

In this project it is used to:

- organize prediction results
- create a dataframe
- export predictions to **predictions.csv**

---

### NumPy (`numpy`)

NumPy provides efficient numerical operations used in machine learning and scientific computing.

---

# How to Run the Project

## Step 1 — Train the Model

```
python train.py
```

This will:

- download the dataset
- train the neural network
- save the trained model

Output generated:

```
fashion_cnn.pth
```

---

## Step 2 — Generate Predictions

```
python predict.py
```

This will:

- load the trained model
- generate predictions
- export results to a CSV file

Output generated:

```
predictions.csv
```

---

# Files Included

| File | Description |
|-----|-------------|
| `model.py` | Defines the CNN neural network architecture |
| `train.py` | Trains the model using the FashionMNIST dataset |
| `predict.py` | Loads the trained model and generates predictions |
| `predictions.csv` | CSV file containing predicted labels |
| `fashion_cnn.pth` | Saved neural network model weights |
| `README.md` | Project documentation |

---

# Project Objective

The objective of this project is to demonstrate how **deep learning models can be used for image classification**. By training a convolutional neural network on image data, the model learns patterns that allow it to categorize clothing items automatically.

---

# Example Applications

Image classification models like this can be used in:

- **E-commerce product categorization**
- **Automated image tagging**
- **Retail inventory management**
- **Computer vision systems**
- **AI-based recommendation systems**

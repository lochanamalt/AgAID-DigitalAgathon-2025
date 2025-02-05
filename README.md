# AgAID Crop Residue Coverage Prediction Challenge - Digital Agathon 2025

This repository contains the solution for the Crop Residue Coverage Prediction Challenge, part of the Digital Agathon 2025 organized by the AgAID Institute.  Our approach utilizes a U-Net architecture for semantic segmentation to distinguish between crop residue and soil in agricultural images.

## Challenge Description

Accurate estimation of crop residue coverage is essential for monitoring soil health, erosion control, and sustainable agricultural practices. This challenge focuses on segmenting images into crop residue and bare soil to determin crop residue coverage percentage in agricultural fields.

## Team Members

* Lochana Marasinghe
* Chamaporn Paiboonvorachat
* William Fralia
* Ehsan Norouzi
* Negar Haghpanahi

## Dataset

* The dataset consists of RGB images labeled with corresponding grayscale segmentation masks.
* The dataset is split into training, validation.

## Solution Overview

Our solution employs a U-Net architecture, a deep learning model well-suited for image segmentation tasks.  We chose U-Net due to its proven effectiveness in capturing contextual information and producing precise segmentation masks.  The model is trained to classify each pixel in an input image as either "crop residue" or "soil."


## Model Architecture

We implemented a U-Net architecture for semantic segmentation. [Optional: Briefly describe the key components of your U-Net implementation, such as the number of layers, filter sizes, activation functions, loss function, and optimizer.]

* **Architecture:** U-Net
* **Loss Function:** Categorical Focal Loss
* **Optimizer:** Adam with a learning rate scheduler
* **Metrics:** Intersection over Union (IoU), Accuracy, Precision, Recall, F1-score

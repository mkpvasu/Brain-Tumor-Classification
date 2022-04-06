# Brain Tumor Classification through MRIs

Hung-An Chen (hungan)

Aditya Nayak (adityamn)

Muni Kumar Pridivi Vasu (mkpvasu)

Austin Sacro (ajsacro)

## Video Walkthrough
[![YouTube link](https://img.youtube.com/vi/6u4weY28X5A/0.jpg)](https://youtu.be/6u4weY28X5A)

## Description

Brain tumors are one of the most serious illnesses which accounts for 85% to 90% of all primary central nervous system (CNS) tumors. During 2020 alone, it has affected nearly 300,000+ people worldwide according to statistics published by Cancer.net. It is also the 10th leading cause of death for men and women. Early detection and accurate understanding of the intricacies in types of the tumor which helps in curing, providing medication and prevention of the disease in future. The radiologists primarily use Magnetic Resonance Imaging (MRI) to analyze brain tumors. This provides an information about whether the brain is normal or abnormal and further aids in identifying the type of it. The advancements in machine learning and computer vision can give an valuable assistance to the doctors in swiftly and precisely determining the presence and type of tumor.

This motivated us take up to classify brain tumors through MRIs by training a neural network model through the [Brain Tumor Classification (MRI)](https://figshare.com/articles/dataset/brain_tumor_dataset/1512427?file=7953679) open source dataset as our project. There are three classifications we'll be working with: Glioma tumor / Meningioma tumor / Pituitary tumor. We'll be using the neural network introduced in lecture and applying different activation functions to test out their accuracies. We might try fitting in multiple layers to increase the overall accuracy and tuning parameters to prevent overfitting of the model. We'll mainly focus on training the model through the brain tumor images in the specified dataset.

## Dataset

The dataset used for our brain tumor classification model is published by Jun Chen. It contains 3064 T1-weighted contrast-inhanced MRI images of patients with three kinds of brain tumor: meningioma (708 slices), glioma (1426 slices), and pituitary tumor (930 slices).

This data is organized in matlab data format (.mat file). Each file stores a struct containing the following fields for an image:

- cjdata.label : 1 for meningioma, 2 for glioma, 3 for pituitary tumor
- cjdata.PID : patient ID
- cjdata.image : image data
- cjdata.tumorBorder : a vector storing the coordinates of discrete points on tumor border
- cjdata.tumorMask : a binary image with 1s indicating tumor region

## Approach
Initially the data has been seggregated to three class types. The train and test set has been split based on the desired ratio (Here, 0.7). 70% of each category of the data will be randomly picked up for the training set and the rest 30% will be categorized to the test data. Then, the images have been converted to tensors alonge with augmenting each image by rotating 90 degrees and vertical flipping the same. This avoids the model to overfit the training data. Here, Resnet50 which is pretrained in ImageNet dataset has been utilized as our model.


## Previous work

Our project was inspired by [Deep Residual Learning for Image Recognition (K. He et al., 2016)](https://arxiv.org/pdf/1512.03385.pdf). We wanted to test and compare the efficiency of the ResNet-50 neural network, both pre-trained and non-pre-trained versions, trained on the [Brain Tumor Classification (MRI)](https://figshare.com/articles/dataset/brain_tumor_dataset/1512427?file=7953679) dataset with variations and optimizations.

## Results
Initially, we ran ResNet with no momentum and weight decay, which resulted in the
network being overfitted to our training dataset. We got ~99% of training accuracy
yet the testing accuracy was merely ~91%. As a result, we ran the model several times
with distinct combinations of optimizer parameters, in an attempt to fine tune with
the best accuracy. It turned out that using `decay=0.01` and `momentum=0.1` gave
the optimal result with a training accuracy of 95.6% and a testing accuracy of 89%. We
noticed that the testing accuracy had space for improvement and inferred that the
size of our training dataset should be larger.

The following graph shows the changes of convolutional losses as the training goes
on (The x-axis shows iterations). We can clearly see that the loss significantly dropped
during the first two epochs and fluctuated below 0.5 during subsequent epochs.

![Itr vs Loss](./loss.png)

## Discussion

Throughout this project, we ran into a few problems and obstacles along the way. 
We were initially running into some size and dimensional input problems using the 
resnet model, but then, we were getting CUDA RuntimeExceptions where we would 
run out of memory. If we were to keep working on the project in the future, one of 
the next steps we would take would be to train our model to learn a fourth classification, 
which would be no tumor. The dataset we used only had three classifications (Glicoma, 
Meningioma, and Pituitary), and initially we wanted to add this fourth classification 
of no tumor, but all of the datasets we found with no tumor were formatted and organized
differently than the dataset we were already using. If we had more time, we would like
to find a dataset for the no tumor classification and augment it to match our existing
dataset.
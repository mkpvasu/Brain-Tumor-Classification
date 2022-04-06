import random

# Define the dataset to be used for training as train_data and test as test_data

train_data = []
test_data = []
img = None
label = None

# Define the ratio of train and test data split (train_test_ratio) in each category of tumors.
# Suppose if the ratio is 0.7, then 70% of images in each category will be added to the training data with shuffling within particular category each time.

train_test_ratio = 0.7

# Splitting the meningioma according to the train_test_ratio and adding them to training data
meningioma_n_split = round(train_test_ratio*len(meningioma))
random.shuffle(meningioma)
for i in range(meningioma_n_split):
  train_data.append(meningioma[i][:])
for j in range(meningioma_n_split,len(meningioma)):
  test_data.append(meningioma[j][:])

# Splitting the glioma according to the train_test_ratio and adding them to training data
glioma_n_split = round(train_test_ratio*len(glioma))
random.shuffle(glioma)
for i in range(glioma_n_split):
  train_data.append(glioma[i][:])
for j in range(glioma_n_split,len(glioma)):
  test_data.append(glioma[j][:])

# Splitting the pituitary according to the train_test_ratio and adding them to training data
pituitary_n_split = round(train_test_ratio*len(pituitary))
random.shuffle(pituitary)
for i in range(pituitary_n_split):
  train_data.append(pituitary[i][:])
for j in range(pituitary_n_split,len(pituitary)):
  test_data.append(pituitary[j][:])

# Splitting the no_class according to the train_test_ratio and adding them to training data
no_class_n_split = round(train_test_ratio*len(no_class))
random.shuffle(no_class)
for i in range(no_class_n_split):
  train_data.append(no_class[i][:])
for j in range(no_class_n_split,len(no_class)):
  test_data.append(no_class[j][:])

# Shuffle data to make our model more robust as it encounters variations each time we run the model
random.shuffle(train_data)

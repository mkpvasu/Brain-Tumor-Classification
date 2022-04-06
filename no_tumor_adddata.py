from PIL import Image

def no_tumor_data():
  dir = 'BrainTumorClassification/no_tumor_train/'
  dir1 = 'BrainTumorClassification/no_tumor_test/'
  label = float(0);
  for filename in os.listdir(dir):
    image = Image.open(dir + filename, 'r')
    no_class.append([image, label])
  for filename in os.listdir(dir1):
    image = Image.open(dir1 + filename, 'r')
    no_class.append([image, label])
    
  return no_class

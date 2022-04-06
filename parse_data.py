import numpy as np
import h5py
import os

def parse_data():
    dir = 'BrainTumorClassification/data/'
    meningioma = []
    glioma = []
    pituitary = []
    no_class = []
    for filename in os.listdir(dir):
        try:
            f = h5py.File(dir + filename,'r')
            data = f['cjdata']
            label = data['label'][0, 0]
            img = np.array(data['image'])
            if label == 1:
                meningioma.append([img,label])
            elif label == 2:
                glioma.append([img,label])
            elif label == 3:
                pituitary.append([img,label])
            else:
                no_class.append([img,label])
        except:
            continue

    print("Data loaded!")
    return (meningioma, glioma, pituitary, no_class)

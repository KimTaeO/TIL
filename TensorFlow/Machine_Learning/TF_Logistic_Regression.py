import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import SGD, Adam

import numpy as np

print(tf.__version__)

# Colab의 /content/gdrive/ 에 Google Drive를 마운트 시킴

from google.colab import drive

drive.mount('/content/gdrive/')

# Google Drive내의 working directory 이동

import os

working_dir = 'dataset'

colab_default_dir = '/content/gdrive/My Drive/Colab Notebooks/'

original_dir = os.getcwd()

try:
    
    os.chdir(colab_default_dir)
    
    if not os.path.exists(working_dir):
        os.mkdir(working_dir)
        
    os.chdir(working_dir)
    print('current dir = ', os.getcwd())
    
except Exception as err:
    
    os.chdir(original_dir)
    print(str(err))

try:
    
    loaded data = np.loadtxt('./diabates.csv', delimiter = ',')
    
    x_data= loaded_data[:0:-1]
    t_data= loaded_data[:,[-1]]
    
    print('x_data.shape = ', x_data.shape)
    print('t_data.shape = ', t_data.shape)
    
    
    except Exception as err:
    
    print(str(err))


model = Sequential()

model.add(Dense(t_data.shape[1],input_shape = (x_data.shape[1], ),activation = 'sigmoid'))

model = Sequential()

model.add(Dense(t_data.shape[1],input_shape = (x_data.shape[1], ),activation = 'sigmoid'))


model.evaluate(x_data, t_data)

import matplotlib.pyplot as plt

plt.title('Loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.grid()

plt.plot(hist.history['loss'], label='train loss')
plt.plot(hist.history['val_loss'], label='validation loss')

plt.legend(loc='best')

plt.show()


import matplotlib.pyplot as plt

plt.title('Accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.grid()

plt.plot(hist.history['accuracy'], label='train accuracy')
plt.plot(hist.history['val_accuracy'], label='validation accuracy')

plt.legend(loc='best')

plt.show()
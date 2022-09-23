{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "\n",
    "from tensorflow.keras.models import Sequential\n",
    "from tensorflow.keras.layers import Flatten, Dense\n",
    "from tensorflow.keras.optimizers import SGD, Adam\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "print(tf.__version__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Colab의 /content/gdrive/ 에 Google Drive를 마운트 시킴\n",
    "\n",
    "from google.colab import drive\n",
    "\n",
    "drive.mount('/content/gdrive/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Google Drive내의 working directory 이동\n",
    "\n",
    "import os\n",
    "\n",
    "working_dir = 'dataset'\n",
    "\n",
    "colab_default_dir = '/content/gdrive/My Drive/Colab Notebooks/'\n",
    "\n",
    "original_dir = os.getcwd()\n",
    "\n",
    "try:\n",
    "    \n",
    "    os.chdir(colab_default_dir)\n",
    "    \n",
    "    if not os.path.exists(working_dir):\n",
    "        os.mkdir(working_dir)\n",
    "        \n",
    "    os.chdir(working_dir)\n",
    "    print('current dir = ', os.getcwd())\n",
    "    \n",
    "except Exception as err:\n",
    "    \n",
    "    os.chdir(original_dir)\n",
    "    print(str(err))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    \n",
    "    loaded data = np.loadtxt('./diabates.csv', delimiter = ',')\n",
    "    \n",
    "    x_data= loaded_data[:0:-1]\n",
    "    t_data= loaded_data[:,[-1]]\n",
    "    \n",
    "    print('x_data.shape = ', x_data.shape)\n",
    "    print('t_data.shape = ', t_data.shape)\n",
    "    \n",
    "    \n",
    "    except Exception as err:\n",
    "    \n",
    "    print(str(err))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = Sequential()\n",
    "\n",
    "model.add(Dense(t_data.shape[1],input_shape = (x_data.shape[1], ),activation = 'sigmoid'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.compile(optimizer=SGD(learning_rate=0.01),loss = 'binary_crossentropy', metrics=['accuracy'])\n",
    "\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hist = model.fit(x_data, t_data, epochs=500, validation_split=0.2, verbose=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.evaluate(x_data, t_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "plt.title('Loss')\n",
    "plt.xlabel('epochs')\n",
    "plt.ylabel('loss')\n",
    "plt.grid()\n",
    "\n",
    "plt.plot(hist.history['loss'], label='train loss')\n",
    "plt.plot(hist.history['val_loss'], label='validation loss')\n",
    "\n",
    "plt.legend(loc='best')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "plt.title('Accuracy')\n",
    "plt.xlabel('epochs')\n",
    "plt.ylabel('accuracy')\n",
    "plt.grid()\n",
    "\n",
    "plt.plot(hist.history['accuracy'], label='train accuracy')\n",
    "plt.plot(hist.history['val_accuracy'], label='validation accuracy')\n",
    "\n",
    "plt.legend(loc='best')\n",
    "\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.6 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "fbe58ca63fe33f9eeae9e71d10368d2b4a57f2b1b395836210cc60d362c66949"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

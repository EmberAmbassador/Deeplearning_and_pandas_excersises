# Oschegow Nicolaj, Bruder Luca
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn import metrics

from tensorflow.keras.datasets import mnist
from tensorflow.keras import models
from tensorflow.keras import layers

# a)

# i)   The activation (function) decides whether a certain input activates the corresponding
#      neuron or not and thus influences the output of that neuron greatly.

# ii)  The optimizer is a method of reducing loss. It updates the various parameters to
#      minimize a given function.

# iii) The loss (function) calculates how far our prediction is from the actual value
#      therefore evaluating how good (or bad) the prediction is.

# iv)  Metrics are certain values by which we want to evaluate our network. In the example
#      from the lecture this could be accuracy as in how accurate the guessed number was.

# v)   An epoch is a full cycle through a given training set. Once the network has seen
#      each value or element of the training set once, the first epoch would be complete.
#      Usually a network is trained on more than one epoch.

# vi)  Batch size refers to the number of values or elements used in a single iteration
#      of the network. The batch size can be the same as the total training set (at which
#      point one batch would be one epoch) but doesn't have to be. 


# b)

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy',metrics=['accuracy'])
train_images_flat = train_images.reshape((60000, 28*28))
test_images_flat = test_images.reshape((10000, 28*28))

train_images_norm = train_images_flat.astype('float32') / 255
test_images_norm = test_images_flat.astype('float32') / 255

from tensorflow.keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images_norm, train_labels, epochs = 5, batch_size=128)

predictions = network.predict(test_images_norm)

cnf_matrix = metrics.confusion_matrix(test_labels.argmax(axis=1), predictions.argmax(axis=1))
print(cnf_matrix)

# The columns dictate the correct number (the expected value) and the rows show the amount of
# guessed numbers. (0, 0) for example shows the amount of zeros, that have been identified as
# such. Accordingly (1, 1) shows the amount of correctly guessed ones and so forth. Thus (1, 8)
# shows the number of ones that have been falsely identified as eights.

# Running the code multiple times yields different confusion matrices. This is due to the fact,
# that the network is newly trained each time you run the code and therefore might be building
# slightly different models. These models in turn might make different predictions at some
# point. Though overall the predictions only differ in very few cases.
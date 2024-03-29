import tensorflow as tf
import numpy as np

print(tf.__version__)


x_data = np.array([2, 4, 6, 8, 10,
                   12, 14, 16, 18, 20]).astype('float32')

t_data = np.array([0, 0, 0, 0, 0,
                   0, 1, 1, 1, 1]).astype('float32')


model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(8, input_shape=(1,), 
                                activation='sigmoid'))


model.add(tf.keras.layers.Dense(1, activation='sigmoid'))


model.compile(tf.keras.optimizers.SGD(learning_rate=0.1),
              loss='binary_crossentropy', metrics=['accuracy'])

model.summary()


hist = model.fit(x_data, t_data, epochs=500)


test_data = np.array([0.5, 3.0, 3.5, 
                      11.0, 13.0, 31.0])

sigmoid_value = model.predict(test_data)

logical_value = tf.cast(sigmoid_value > 0.5,
                      dtype=tf.float32)

for i in range(len(test_data)):
    print(test_data[i], 
          sigmoid_value[i], 
          logical_value.numpy()[i])



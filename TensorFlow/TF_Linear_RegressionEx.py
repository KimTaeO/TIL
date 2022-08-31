import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import SGD,Adam

import numpy as np

print(tf.__version__)


# 데이터 생성
x_data = np.array([[1,2,0],[5,4,3],[1,2,-1],[3,1,0],[2,4,2],
                  [4,1,2],[-1,3,2],[4,3,3],[0,2,6],[2,2,1],
                  [1,-2,-2],[0,1,3],[1,1,3],[0,1,4],[2,3,3]])
                  
t_data = np.array([-4, 4, -6, 3,-4,
                  9, -7, 5, 6, 0,
                  4, 3, 5, 5, 1])   

print('x_data.shape = ', x_data.shape, ',t_data.shape = ', t_data.shape)


# 모델 구축
model = Sequential()

model.add(Dense(1, input_shape=(3, ), activation='linear'))


# 모델 컴파일

model.compile(optimizer=SGD(learning_rate=1e-2), loss='mse')

model.summary()


# 모델 학습

hist = model.fit(x_data, t_data, epochs=1000)


# 모델 평가 및 예측
test_data = [[5,5,0], [2,3,1], [-1,0,-1],[10,5,2], [4,-1,2]]

ret_val = [2*data[0]-3*data[1]+2*data[2] for data in test_data]

prediction_val = model.predict(np.array(test_data))

print(prediction_val)
print('==============')
print(ret_val)

print(model.input)  # 모델 입력
print(model.output)  # 모델 출력
print(model.weights) # 모델 가중치

# 모델 손실함수 추세
import matplotlib.pyplot as pit

pit.title("Loss Trend")
pit.xlabel("epochs")
pit.ylabel('loss')
pit.grid()

pit.plot(hist.history['loss'], label='train loss')
pit.legend(loc='best')

pit.show()
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from pandas_datareader import data

"""
 Practice04 - 선형회귀  주가데이터
"""

# 1. 노드생성
def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    return numerator / (denominator + 1e-7)

stock = data.DataReader("KRX:000060", "google")
stock = stock.as_matrix()
stock = MinMaxScaler(stock)

x_data = stock[:,0:2]
y_data = stock[:,[4]]

X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 1])
 
W = tf.Variable(tf.random_normal([2,1]))
b = tf.Variable(tf.random_normal([1]))
  
# 가설과 코스트
hypothesis = tf.matmul(X, W) + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))
  
# 최적화 
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)
  
# 2. 세션생성
sess = tf.Session();
sess.run(tf.global_variables_initializer())
  
# 3. 세션실행 !
sess.run(tf.global_variables_initializer())
for step in range(20001) :
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y:y_data})
    if step % 50 == 0 :
        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
sess.close()

plt.plot(y_data)
plt.plot(hy_val)
plt.show()
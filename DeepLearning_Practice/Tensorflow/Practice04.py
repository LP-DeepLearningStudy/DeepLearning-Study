import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

"""
 Practice04 - 선형회귀 
"""

# 1. 노드생성

x_data = [[1.,2.,3.],[4.,5.,6.]]
y_data = [[1.],[22.]]

X = tf.placeholder(tf.float32, [None, 3])
Y = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.random_normal([3,1]))
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
for step in range(2001) :
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y:y_data})
    if step % 10 == 0 :
        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
sess.close()
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

"""
 Practice03 - 
 참고자료 : https://github.com/golbin/TensorFlow-Tutorials/blob/master/03%20-%20TensorFlow%20Basic/02%20-%20Variable.py
"""

# 1. 노드생성
A = tf.placeholder(tf.float32, [None, 3])
print(A)

a_data = [[1,2,3],[4,5,6]]

W = tf.Variable(tf.random_normal([3,2]))
b = tf.Variable(tf.random_normal([2,1]))

expr = tf.matmul(A, W) + b

# 2. 세션생성
sess = tf.Session();

# 3. 세션실행 !
sess.run(tf.global_variables_initializer())
print(sess.run(expr, feed_dict={A:a_data}))
sess.close()
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

"""
 Practice02 - 텐서플로우의  placeholder 와 기본 연산
"""

# 1. 노드생성
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

# 사칙연산
calcNode01 = tf.add(a, b)
calcNode02 = tf.subtract(a, b)
calcNode03 = tf.multiply(a, b)
calcNode04 = tf.divide(a, b)

# 2. 세션생성
sess = tf.Session();

# 3. 세션실행 !
print("더하기 연산 : ",sess.run(calcNode01, feed_dict={a:3, b:5}),"\n")
print("빼기 연산 : ",sess.run(calcNode02, feed_dict={a:3, b:5}),"\n")
print("곱하기 연산: ",sess.run(calcNode03, feed_dict={a:3, b:5}),"\n")
print("나누기 연산: ",sess.run(calcNode04, feed_dict={a:3, b:5}),"\n")
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

"""
 Practice02 - 텐서플로우의  placeholder 와 기본 연산
"""

# 1. 노드생성
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
calcNode = tf.add(a, b)

# 2. 세션생성
sess = tf.Session();

# 3. 세션실행 !
print(sess.run(calcNode, feed_dict={a:3, b:5}))
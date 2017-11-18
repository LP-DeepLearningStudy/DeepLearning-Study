import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

"""
 Practice01 - 텐서플로우의 기본 구조
"""

# 1. 노드생성
hello = tf.constant("Hello world !")

# 2. 세션생성
sess = tf.Session();

# 3. 세션실행 !
print(sess.run(hello))
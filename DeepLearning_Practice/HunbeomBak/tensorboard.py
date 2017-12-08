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
with tf.name_scope("add") as scope:
    calcNode01 = tf.add(a, b)
    cal1_hist = tf.summary.histogram("add",calcNode01 )

with tf.name_scope("sub") as scope:
    calcNode02 = tf.subtract(a, b)
    cal1_hist = tf.summary.histogram("sub",calcNode02 )

with tf.name_scope("mult") as scope:
    calcNode03 = tf.multiply(a, b)
    cal1_hist = tf.summary.histogram("mult",calcNode03 )
    
with tf.name_scope("div") as scope:
    calcNode04 = tf.divide(a, b)
    cal1_hist = tf.summary.histogram("div",calcNode04 ) 

# 2. 세션생성
with tf.Session() as sess:
    # tensorboard --logdir=./logs/xor_logs
    merged_summary = tf.summary.merge_all()
    writer = tf.summary.FileWriter("./logs/xor_logs")
    writer.add_graph(sess.graph)  # Show the graph

# 3. 세션실행 !
    print("더하기 연산 : ",sess.run(calcNode01, feed_dict={a:3, b:5}),"\n")
    print("빼기 연산 : ",sess.run(calcNode02, feed_dict={a:3, b:5}),"\n")
    print("곱하기 연산: ",sess.run(calcNode03, feed_dict={a:3, b:5}),"\n")
    print("나누기 연산: ",sess.run(calcNode04, feed_dict={a:3, b:5}),"\n")
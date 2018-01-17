# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 23:46:04 2017

@author: 박훈범

당뇨병 예측하기

자료 출처 및 참고사이트 : 모두의 딥러닝
"""
import tensorflow as tf
import numpy as np

#파일 불러오기
xy = np.loadtxt('data-03-diabetes.csv', delimiter=',', dtype=np.float32)

#train 셋 설정
x_train = xy[:, 0:-1]
y_train = xy[:, [-1]]   

#train 셋 모양 확인
print(x_train.shape, y_train.shape)
# x: (759.8) / y: (759.1) 

# 선언
X = tf.placeholder(tf.float32, shape=[None, 8])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.get_variable("W",shape=[8, 1],initializer=tf.contrib.layers.xavier_initializer())
b = tf.Variable(tf.random_normal([1]), name='bias')

#가설(Hypothesis)
H = tf.sigmoid(tf.matmul(X, W) + b)

#코스트 함수
cost = -tf.reduce_mean(Y * tf.log(H) + (1 - Y) *tf.log(1 - H))

#기울기 감소법
train = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

predicted = tf.cast(H > 0.5, dtype=tf.float32) #예측값이 0.5넘으면 pass, 아니면 false
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32)) #맞춘거 평균냄

#그래프 실행
sess=tf.Session()

#변수 초기화
sess.run(tf.global_variables_initializer())

#학습
feed_dict={X: x_train, Y: y_train}
for step in range(10001):
    cost_val, _ = sess.run([cost, train], feed_dict=feed_dict)
    if step % 200 == 0:
        print(step, cost_val)

print("\n학습종료!\n")
# Accuracy report
h, c, a = sess.run([H, predicted, accuracy],feed_dict=feed_dict)

print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)





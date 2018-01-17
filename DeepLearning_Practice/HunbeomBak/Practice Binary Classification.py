# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:25:52 2017

@author: Hunbeom Bak

참고 : 모두를 위한 딥러닝
데이터 출처: https://www.kaggle.com/ibjohnsson/simple-binary-classification/data



현재 학습 시키면 학습이 안됨
learning rate 수정 및 normaliziation 해야함
"""
import numpy as np
import tensorflow as tf


#파일 불러오기
xy = np.genfromtxt('creditcard.csv', delimiter=',', dtype=np.float32, skip_header =1)
#skip_header: 첫번째 줄은 무슨 데이터인지 알려주는 문자열, 따라서 불오는것을 생략함

def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    # noise term prevents the zero division
    return numerator / (denominator + 1e-7)

xy = MinMaxScaler(xy)

#train 셋 설정
x_train = xy[:, 0:-1]
y_train = xy[:, [-1]]   

#train 셋 모양 확인
print(x_train.shape, y_train.shape)
#(284807, 30) (284807, 1)

# 선언
X = tf.placeholder(tf.float32, shape=[None, 30])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([30, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#가설(Hypothesis)
H = tf.sigmoid(tf.matmul(X, W) + b)

#코스트 함수
cost = -tf.reduce_mean(Y * tf.log(H) + (1 - Y) *tf.log(1 - H))

#기울기 감소법
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)


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

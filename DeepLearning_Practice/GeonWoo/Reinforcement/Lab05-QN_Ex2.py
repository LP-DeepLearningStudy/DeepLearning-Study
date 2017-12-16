import gym
<<<<<<< HEAD
env = gym.make('CartPole-v0')
env.reset()
random_episodes = 0
reward_sum = 0
while random_episodes < 10 :
    env.render()
    action = env.action_space.sample()
    observation, reward, done, _ = env.step(action)
    print(observation, reward, done)
    reward_sum += reward
    if done :
        random_episodes += 1
        print("Reward for this episodes: ", reward_sum)
        reward_sum = 0
        env.reset()
=======
import tensorflow as tf
import numpy as np

env = gym.make('CartPole-v0')

learning_rate = 1e-1
input_size = env.observation_space.shape[0]
output_size = env.action_space.n

X = tf.placeholder(tf.float32, [None, input_size], name="input_x")

W1 = tf.get_variable("W1", shape=[input_size, output_size], initializer=tf.contrib.layers.xavier_initializer())
Qpred = tf.matmul(X, W1)

Y = tf.placeholder(shape=[None, output_size], dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y-Qpred))
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

num_episodes = 2000
dis = 0.9
rList = []

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(num_episodes) :
    e = 1. / ((i/10)+1)
    rAll = 0
    step_count = 0
    s = env.reset()
    done = False

    while not done :
        step_count += 1
        x = np.reshape(s, [1, input_size])
        Qs = sess.run(Qpred, feed_dict={X: x})
        if np.random.rand(1) < e :
            a = env.action_space.sample()
        else :
            a = np.argmax(Qs)

        s1, reward, done, _ = env.step(a)
        if done :
            x1 = np.reshape(s1, [1, input_size])
            Qs1 = sess.run(Qpred, feed_dict={X:x1})
            Qs[0, a] = reward + dis * np.max(Qs1)
        sess.run(train, feed_dict={X:x, Y:Qs})
        s = s1

    rList.append(step_count)
    print("Episode: {} steps: {}".format(i, step_count))
    if len(rList) > 10 and np.mean(rList[-10:]) > 500 :
        break;

observation = env.reset()
reward_sum = 0
while True :
    env.render()

    x = np.reshape(observation, [1, input_size])
    Qs = sess.run(Qpred, feed_dict={X:x})
    a = np.argmax(Qs)

    observation, reward, done, _ = env.step(a)
    reward_sum += reward
    if done :
        print("Total Score: {}".format(reward_sum))
        break
>>>>>>> f0d3d33cc59412638c8426062538d5427fb68563

import gym
from gym.envs.registration import register
import numpy as np
import matplotlib.pyplot as plt
import random as pr

register(
    id="FrozenLake-v3",
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs = {'map_name' : '4x4',
            'is_slippery': True}
)
env = gym.make('FrozenLake-v3')

Q = np.zeros([env.observation_space.n, env.action_space.n])
num_episodes = 2000
dis = .99
learning_rate = .85

rList = []

for i in range(num_episodes) :
    state = env.reset()
    rAll = 0
    done = False

    while not done :
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) / (i + 1))
        new_state, reward, done, _ = env.step(action)
        Q[state,action] = (1 -learning_rate) * Q[state,action] \
          + learning_rate * (reward + dis * np.max(Q[new_state, :]))

        rAll += reward
        state = new_state

    rList.append(rAll)

print("Success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print(Q)
plt.plot(range(len(rList)), rList, color="red")
plt.show()
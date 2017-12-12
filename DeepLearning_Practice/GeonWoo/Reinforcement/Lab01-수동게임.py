import gym
from gym.envs.registration import register
import sys, msvcrt

arrow_keys = {
    b'8': 3,
    b'2': 1,
    b'6': 2,
    b'4': 0
}

register(
    id="FrozenLake-v3",
    entry_point = "gym.envs.toy_text:FrozenLakeEnv",
    kwargs={'map_name' : '4x4', 'is_slippery' : False}
)

env = gym.make('FrozenLake-v3')
env.render()

while True :
    key = msvcrt.getch()
    print(key)
    if key not in arrow_keys.keys() :
        print("Game aborted!")
        break2

    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render()
    print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

    if done :
        print("Finised with reward", reward)
        break
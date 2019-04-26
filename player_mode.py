import ppaquette_gym_super_mario as mario
import gym

import keyboard


key_map = 'wasdpl'
action = [0, 0, 0, 0, 0, 0]

env = gym.make('ppaquette/SuperMarioBros-1-1-v0')
env.reset()


def keyevent_handler(old_action):
    if keyboard.is_pressed('esc'):
        exit(1)
    for idx, key in enumerate(key_map):
        if keyboard.is_pressed(key):
            old_action[idx] = 1
        else:
            old_action[idx] = 0
    return old_action


while True:
    env.render()

    action = keyevent_handler(action)
    state, reward, is_finished, info = env.step(action)
    print('reward: {} / is_finished: {} / info: {}'.format(reward, is_finished, info))

env.close()


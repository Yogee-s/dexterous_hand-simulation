import click
import pickle
import numpy as np
import random

DESC = '''
Helper script to visualize learning.\n
USAGE:\n
    Visualizes learning on the env\n
    $ python visualize_policy --env_name relocate --object_name potted_meat_can \n
'''

from hand_imitation.env.environments.ycb_relocate_env import YCBRelocate
from hand_imitation.env.environments.mug_pour_water_env import WaterPouringEnv
from hand_imitation.env.environments.mug_place_object_env import MugPlaceObjectEnv

# List of available objects
objects = ['sugar_box','tomato_soup_can', 'mustard_bottle', 'potted_meat_can', 'banana', 'mug', 'large_clamp', 'foam_brick']

# MAIN =========================================================
@click.command(help=DESC)
@click.option('--env_name', type=str, help='environment to load', required=True)
def main(env_name):
    friction = (1, 0.5, 0.01)
    T = 100  # Default number of steps

    if "best" in env_name or "test" in env_name:
        policy = f"../trained_model/{env_name}.pickle"
    elif env_name == "relocate":
        policy = f"../pretrained_model/{env_name}-{{object_name}}.pickle"
    else:
        policy = f"../{env_name}.pickle"

    pi = pickle.load(open(policy, 'rb'))

    object_name = random.choice(objects)
    e = YCBRelocate(has_renderer=True, object_name=object_name, friction=friction, object_scale=0.8,
                    solref="-6000 -300", randomness_scale=0.25)

    for _ in range(100):
        object_name = random.choice(objects)
        e.set_object(object_name)
        e.sim.forward()  # Ensure Mujoco simulation updates
        state, done = e.reset(), False
        step = 0
        reward_sum = 0
        
        while True:
            step += 1
            if step >= T:
                break

            action = pi.get_action(state)[1]['evaluation']

            state, reward, done, _ = e.step(action)
            e.render()  # Render after each step to visualize the environment
            reward_sum += reward
        
        print(f'Total reward for object {object_name}: {reward_sum}')

if __name__ == '__main__':
    main()

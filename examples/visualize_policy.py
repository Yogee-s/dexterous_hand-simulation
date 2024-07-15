import click
import pickle
import numpy as np

DESC = '''
Helper script to visualize learning.\n
USAGE:\n
    Visualizes learning on the env\n
    $ python visualize_policy --env_name relocate --object_name potted_meat_can \n
'''
from hand_imitation.env.environments.ycb_relocate_env import YCBRelocate
from hand_imitation.env.environments.mug_pour_water_env import WaterPouringEnv
from hand_imitation.env.environments.mug_place_object_env import MugPlaceObjectEnv



# MAIN =========================================================
@click.command(help=DESC)
@click.option('--env_name', type=str, help='environment to load', required=True)
@click.option('--object_name', type=str, help='environment to load', required=False, default=None)
def main(env_name, object_name):
    friction = (1, 0.5, 0.01)

    if env_name == "relocate":
        if object_name is None:
            raise ValueError("For relocate task, object name is needed.")
        e = YCBRelocate(has_renderer=True, object_name=object_name, friction=friction, object_scale=0.8,
                        solref="-6000 -300", randomness_scale=0.25)
        T = 100
    elif env_name == "pour":
        e = WaterPouringEnv(has_renderer=True, scale=1.0, tank_size=(0.15, 0.15, 0.08))
        T = 200
    elif env_name == "place_inside":
        e = MugPlaceObjectEnv(has_renderer=True, object_scale=0.8, mug_scale=1.5)
        T = 200

    elif "test" in env_name:
        if object_name is None:
            raise ValueError("For relocate task, object name is needed.")
        e = YCBRelocate(has_renderer=True, object_name=object_name, friction=friction, object_scale=0.8,
                        solref="-6000 -300", randomness_scale=0.25)
        T = 100
    
    else:
        if object_name is None:
            object_name= "mug"
        e = YCBRelocate(has_renderer=True, object_name=object_name, friction=friction, object_scale=0.8,
                        solref="-6000 -300", randomness_scale=0.25)
        T = 100
    


    if "iterations" in env_name:
        # policy = f"training_log/dapg_relocate-mug-0.8_relocate-mug_0.1_100_trpo_seed200/iterations/{env_name}.pickle"
        policy = f"training_log/dapg_relocate-mustard_bottle-0.8_relocate-mustard_bottle_0.1_100_trpo_seed200/{env_name}.pickle"

    elif "test" in env_name:
        policy = f"../trained_model/{env_name}.pickle"

    elif env_name == "relocate":
        policy = f"../pretrained_model/{env_name}-{object_name}.pickle"

    else:
        policy = f"../{env_name}.pickle"

    pi = pickle.load(open(policy, 'rb'))
    for _ in range(100):
        state, done = e.reset(), False
        step = 0
        reward_sum = 0
        while True:
            step += 1
            if step >= T:
                break
            
            ###################################################################################
            ###################################################################################
            # Attempted to use pre-trained adroit model on inspire hand
            ###################################################################################
            ###################################################################################
            # obs_indexes = [0, 1, 2, 3, 4, 5, 9, 10, 13, 14, 17, 18, 22, 23, 25, 26, 28, 29, 
            #                30, 31, 32, 33, 34, 35, 36, 37, 38]
            
            # pi.obs_var = pi.obs_var[obs_indexes]  # Select observation indexes
            # pi.m = 18
            # pi.model.act_dim = 18
            # pi.n = 27
            # pi.model.obs_dim = 27
            # pi.set_transformations()
            # print(f"pi.obs_var.data is: \n{pi.obs_var.data}\n")

            # indexes = [0, 1, 2, 3, 4, 5, 9, 10, 13, 14, 17, 18, 22, 23, 25, 26, 28, 29]
            # action = [pi.get_action(state)[1]['evaluation'][i] for i in indexes]
            ###################################################################################
            ###################################################################################
            # action = pi.get_action(state)[1]['evaluation'][np.random.randint(0,30,18)]
            # action = pi.get_action(state)[1]['evaluation'][0:18]
            # print(f"action is:{action}")
            ###################################################################################
            ###################################################################################

            action = pi.get_action(state)[1]['evaluation']

            state, reward, done, _ = e.step(action)
            for _ in range(2):
                e.render()
            reward_sum += reward
        print(f'total reward {reward_sum}')


if __name__ == '__main__':
    main()

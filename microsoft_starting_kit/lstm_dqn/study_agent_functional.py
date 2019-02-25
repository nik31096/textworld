import gym
from pathlib import Path
from pprint import pprint as print
import textworld

from custom_agent import CustomAgent
from train import _validate_requested_infos

# games 
train_dir = Path('../tw_train_data/train/')
games = [str(file.relative_to(".")) for file in train_dir.iterdir() if file.suffix == '.ulx'][0]
print(games)
print('../tw_train_data/train/tw-cooking-recipe2+cut+drop+go12-XQ7oC7pxS1OPsy6D.ulx')

agent = CustomAgent()
requested_infos = agent.select_additional_infos()
_validate_requested_infos(requested_infos)

env_id = textworld.gym.register_games(["../tw_train_data/train/tw-cooking-recipe2+cut+drop+go12-XQ7oC7pxS1OPsy6D.ulx"], requested_infos,
                                      max_episode_steps=agent.max_nb_steps_per_episode,
                                      name="training")
env_id = textworld.gym.make_batch(env_id, batch_size=agent.batch_size, parallel=True)
env = gym.make(env_id)

state, infos = env.reset()
print(infos)


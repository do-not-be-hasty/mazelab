from gym.envs.registration import register
from gym_maze.envs.generators import SimpleMazeGenerator, RandomMazeGenerator, RandomBlockMazeGenerator, UMazeGenerator, TMazeGenerator, WaterMazeGenerator

register(
    id='MazeEnv-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={
        'maze_generator':RandomMazeGenerator,
        'width':9,
        'height':9,
        'complexity':.5,
        'density':.5,
        'seed':7,
        'obs_type':'discrete',
        'reward_type':'sparse',
        'step_limit':1000,
    }
)

register(
    id='MazeEnv-v1',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={
        'maze_generator':RandomMazeGenerator,
        'width':21,
        'height':21,
        'complexity':.5,
        'density':.5,
        'seed':10,
        'obs_type':'discrete',
        'reward_type':'l2',
        'step_limit':1000,
    }
)

register(
    id='GoalMazeEnv-v0',
    entry_point='gym_maze.envs:GoalMazeEnv',
    kwargs={
        'maze_generator':RandomMazeGenerator,
        'width':7,
        'height':7,
        'complexity':.5,
        'density':.5,
        'seed':9,
        'obs_type':'discrete',
    }
)

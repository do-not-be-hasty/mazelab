from gym.envs.registration import register
from gym_maze.envs.generators import SimpleMazeGenerator, RandomMazeGenerator, RandomBlockMazeGenerator, UMazeGenerator, TMazeGenerator, WaterMazeGenerator

register(
    id='MazeEnv-v0',
    entry_point='gym_maze.envs:MazeEnv',
    kwargs={
        'maze_generator':RandomMazeGenerator,
        'width':7,
        'height':7,
        'complexity':.5,
        'density':.5,
        'seed':5
    }
)

import gymnasium as gym
from gymnasium import spaces

DEFAULT_INITAL_FPS = 60

class SnakeGameEnv(gym.Env):
    def __init__(self) -> None:
        metadata = {"render_modes": ["human", "rgb_array"], "render_fps": DEFAULT_INITAL_FPS}
        super(SnakeGameEnv, self).__init__()
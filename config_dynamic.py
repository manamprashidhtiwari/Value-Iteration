# config_dynamic.py - Dynamic Configuration from User Input

# This file will be populated by user input
# Default values (will be overwritten)

GRID_ROWS = 4
GRID_COLS = 4

GOAL_STATE = (0, 3)
FIRE_STATE = (1, 3)
OBSTACLES = [(1, 1)]
START_STATE = (3, 0)

GOAL_REWARD = 1.0
FIRE_REWARD = -1.0
STEP_REWARD = 0.0

GAMMA = 0.9
THETA = 0.001
MAX_ITERATIONS = 100

ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

def set_configuration(config):
    """Set configuration from user input dictionary"""
    global GRID_ROWS, GRID_COLS, GOAL_STATE, FIRE_STATE, OBSTACLES, START_STATE
    global GAMMA, THETA, MAX_ITERATIONS
    
    GRID_ROWS = config['rows']
    GRID_COLS = config['cols']
    GOAL_STATE = config['goal']
    FIRE_STATE = config['fire']
    OBSTACLES = config['obstacles']
    START_STATE = config['start']
    GAMMA = config['gamma']
    THETA = config['theta']
    MAX_ITERATIONS = config['max_iterations']

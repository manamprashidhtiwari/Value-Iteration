# environment.py - Grid World Environment

import config_dynamic as config

class GridWorld:
    """Simple Grid World Environment"""
    
    def __init__(self):
        self.rows = config.GRID_ROWS
        self.cols = config.GRID_COLS
        self.goal = config.GOAL_STATE
        self.fire = config.FIRE_STATE
        self.obstacles = config.OBSTACLES if config.OBSTACLES else []
        
    def is_valid_state(self, row, col):
        """Check if state is within bounds and not an obstacle"""
        if row < 0 or row >= self.rows:
            return False
        if col < 0 or col >= self.cols:
            return False
        if (row, col) in self.obstacles:
            return False
        return True
    
    def is_terminal(self, state):
        """Check if state is terminal (goal or fire)"""
        if state == self.goal:
            return True
        if self.fire and state == self.fire:
            return True
        return False
    
    def get_possible_actions(self, state):
        """Get valid actions from current state"""
        if self.is_terminal(state):
            return []
        
        row, col = state
        actions = []
        
        # Check each direction
        if self.is_valid_state(row - 1, col):  # UP
            actions.append('UP')
        if self.is_valid_state(row + 1, col):  # DOWN
            actions.append('DOWN')
        if self.is_valid_state(row, col - 1):  # LEFT
            actions.append('LEFT')
        if self.is_valid_state(row, col + 1):  # RIGHT
            actions.append('RIGHT')
        
        return actions
    
    def get_next_state(self, state, action):
        """Get next state after taking action"""
        row, col = state
        
        if action == 'UP':
            return (row - 1, col)
        elif action == 'DOWN':
            return (row + 1, col)
        elif action == 'LEFT':
            return (row, col - 1)
        elif action == 'RIGHT':
            return (row, col + 1)
        
        return state  # Should not reach here
    
    def get_reward(self, state):
        """Get reward for being in a state"""
        if state == self.goal:
            return config.GOAL_REWARD
        elif self.fire and state == self.fire:
            return config.FIRE_REWARD
        else:
            return config.STEP_REWARD
    
    def get_all_states(self):
        """Get all valid states in the grid"""
        states = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_valid_state(row, col):
                    states.append((row, col))
        return states

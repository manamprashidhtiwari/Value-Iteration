# value_iteration.py - Value Iteration Algorithm

import config_dynamic as config
from environment import GridWorld

class ValueIteration:
    """Value Iteration Algorithm for Grid World"""
    
    def __init__(self, env):
        self.env = env
        self.V = {}  # Value function
        self.policy = {}  # Optimal policy
        self.history = []  # Store V for each iteration
        
        # Initialize value function to 0
        for state in self.env.get_all_states():
            self.V[state] = 0.0
        
        # Store initial state
        self.history.append(self.V.copy())  
    
    def calculate_q_value(self, state, action):
        """Calculate Q(s,a) = R(s,a) + γ * V(s')"""
        next_state = self.env.get_next_state(state, action)
        
        # Immediate reward is from the next state (or 0 for normal transitions)
        if next_state == self.env.goal:
            reward = self.env.get_reward(next_state)
            # Terminal state, no future value
            q_value = reward
        elif self.env.fire and next_state == self.env.fire:
            reward = self.env.get_reward(next_state)
            # Terminal state, no future value
            q_value = reward
        else:
            reward = self.env.get_reward(state)
            q_value = reward + config.GAMMA * self.V[next_state]
        
        return q_value
    
    def run(self, max_iterations=None):
        """Run Value Iteration until convergence"""
        if max_iterations is None:
            max_iterations = config.MAX_ITERATIONS
        
        iteration = 0
        
        print("\n--- Value Iteration Started ---\n")
        
        while iteration < max_iterations:
            iteration += 1
            V_new = self.V.copy()
            max_change = 0
            
            # Update value for each state
            for state in self.env.get_all_states():
                # Terminal states have fixed values
                if self.env.is_terminal(state):
                    continue
                
                # Get possible actions
                actions = self.env.get_possible_actions(state)
                if not actions:
                    continue
                
                # Calculate Q-value for each action
                q_values = []
                for action in actions:
                    q = self.calculate_q_value(state, action)
                    q_values.append(q)
                
                # Take maximum
                V_new[state] = max(q_values)
                
                # Track maximum change
                change = abs(V_new[state] - self.V[state])
                max_change = max(max_change, change)
            
            # Store history for visualization
            self.history.append(self.V.copy())
            
            # Update value function
            self.V = V_new
            
            print(f"Iteration {iteration}: max_change = {max_change:.6f}")
            
            # Check convergence
            if max_change < config.THETA:
                print(f"\n✅ Converged after {iteration} iterations!")
                print(f"   (Convergence threshold θ = {config.THETA})")
                break
        else:
            print(f"\n⚠️  Reached maximum iterations ({max_iterations}) without full convergence")
            print(f"   Final max_change = {max_change:.6f}, threshold θ = {config.THETA}")
        
        # Extract optimal policy
        self.extract_policy()
        
        print(f"\n📊 Total iterations completed: {iteration}")
        
        return iteration
    
    def extract_policy(self):
        """Extract optimal policy from value function"""
        for state in self.env.get_all_states():
            if self.env.is_terminal(state):
                self.policy[state] = None
                continue
            
            actions = self.env.get_possible_actions(state)
            if not actions:
                self.policy[state] = None
                continue
            
            # Find best action
            best_action = None
            best_value = float('-inf')
            
            for action in actions:
                q = self.calculate_q_value(state, action)
                if q > best_value:
                    best_value = q
                    best_action = action
            
            self.policy[state] = best_action
    
    def get_value_grid(self, iteration=None):
        """Get value function as 2D grid for specific iteration"""
        if iteration is not None and iteration < len(self.history):
            V = self.history[iteration]
        else:
            V = self.V
        
        grid = [[0.0 for _ in range(self.env.cols)] for _ in range(self.env.rows)]
        
        for state in self.env.get_all_states():
            row, col = state
            grid[row][col] = V[state]
        
        return grid
    
    def get_policy_grid(self):
        """Get policy as 2D grid"""
        grid = [['' for _ in range(self.env.cols)] for _ in range(self.env.rows)]
        
        for state in self.env.get_all_states():
            row, col = state
            action = self.policy.get(state)
            
            if action == 'UP':
                grid[row][col] = '↑'
            elif action == 'DOWN':
                grid[row][col] = '↓'
            elif action == 'LEFT':
                grid[row][col] = '←'
            elif action == 'RIGHT':
                grid[row][col] = '→'
            elif state == self.env.goal:
                grid[row][col] = 'G'
            elif self.env.fire and state == self.env.fire:
                grid[row][col] = 'F'
            else:
                grid[row][col] = '·'
        
        # Mark obstacles
        for obs in self.env.obstacles:
            row, col = obs
            grid[row][col] = 'X'
        
        return grid

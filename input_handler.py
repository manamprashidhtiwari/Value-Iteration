# input_handler.py - Interactive User Input Handler

def get_grid_dimensions():
    """Get grid dimensions from user"""
    print("\n" + "="*50)
    print("   GRID SETUP")
    print("="*50)
    
    while True:
        try:
            dims = input("\nEnter grid dimensions (rows cols): ").strip().split()
            if len(dims) != 2:
                print("❌ Please enter exactly 2 numbers (rows and cols)")
                continue
            
            rows, cols = int(dims[0]), int(dims[1])
            
            if rows < 2 or cols < 2:
                print("❌ Grid must be at least 2x2")
                continue
            if rows > 20 or cols > 20:
                print("❌ Grid too large! Maximum 20x20")
                continue
            
            print(f"✅ Grid size: {rows}x{cols}")
            return rows, cols
        except ValueError:
            print("❌ Invalid input. Please enter two integers.")

def get_state_input(prompt, rows, cols):
    """Get a single state (row, col) from user"""
    while True:
        try:
            state_input = input(prompt).strip().split()
            if len(state_input) != 2:
                print("❌ Please enter exactly 2 numbers (row col)")
                continue
            
            row, col = int(state_input[0]), int(state_input[1])
            
            if row < 0 or row >= rows or col < 0 or col >= cols:
                print(f"❌ State out of bounds! Must be between (0,0) and ({rows-1},{cols-1})")
                continue
            
            return (row, col)
        except ValueError:
            print("❌ Invalid input. Please enter two integers.")

def get_goal_state(rows, cols):
    """Get goal state from user"""
    print(f"\n📍 Goal State (reward: +1)")
    state = get_state_input("Enter goal state (row col): ", rows, cols)
    print(f"✅ Goal: {state}")
    return state

def get_fire_state(rows, cols, goal):
    """Get fire state from user"""
    print(f"\n🔥 Fire State (reward: -1) [Optional]")
    response = input("Do you want a fire state? (yes/no) [no]: ").strip().lower()
    
    if response in ['yes', 'y']:
        while True:
            state = get_state_input("Enter fire state (row col): ", rows, cols)
            if state == goal:
                print("❌ Fire cannot be at the same location as goal!")
                continue
            print(f"✅ Fire: {state}")
            return state
    else:
        print("✅ No fire state")
        return None

def get_obstacles(rows, cols, goal, fire):
    """Get obstacle states from user"""
    print(f"\n🚧 Obstacles [Optional]")
    response = input("Do you want obstacles? (yes/no) [no]: ").strip().lower()
    
    if response not in ['yes', 'y']:
        print("✅ No obstacles")
        return []
    
    obstacles = []
    print("Enter obstacles one by one. Press Enter without input when done.")
    
    obstacle_num = 1
    reserved = [goal]
    if fire:
        reserved.append(fire)
    
    while True:
        try:
            obs_input = input(f"Obstacle {obstacle_num} (row col) or [Enter to finish]: ").strip()
            
            if not obs_input:  # Empty input means done
                break
            
            state_input = obs_input.split()
            if len(state_input) != 2:
                print("❌ Please enter exactly 2 numbers (row col)")
                continue
            
            row, col = int(state_input[0]), int(state_input[1])
            
            if row < 0 or row >= rows or col < 0 or col >= cols:
                print(f"❌ Out of bounds! Must be between (0,0) and ({rows-1},{cols-1})")
                continue
            
            obs = (row, col)
            
            if obs in reserved:
                print("❌ Cannot place obstacle at goal/fire state!")
                continue
            
            if obs in obstacles:
                print("❌ Obstacle already added!")
                continue
            
            obstacles.append(obs)
            reserved.append(obs)
            print(f"✅ Obstacle {obstacle_num} added: {obs}")
            obstacle_num += 1
            
        except ValueError:
            print("❌ Invalid input. Please enter two integers.")
    
    print(f"✅ Total obstacles: {len(obstacles)}")
    return obstacles

def get_start_state(rows, cols, goal, fire, obstacles):
    """Get starting state from user"""
    print(f"\n🎯 Start State [Optional]")
    response = input("Do you want to specify a start state? (yes/no) [no]: ").strip().lower()
    
    if response not in ['yes', 'y']:
        print("✅ No specific start state (for visualization only)")
        return None
    
    reserved = [goal]
    if fire:
        reserved.append(fire)
    reserved.extend(obstacles)
    
    while True:
        state = get_state_input("Enter start state (row col): ", rows, cols)
        
        if state in reserved:
            print("❌ Cannot start at goal/fire/obstacle!")
            continue
        
        print(f"✅ Start: {state}")
        return state

def get_algorithm_parameters():
    """Get algorithm parameters from user"""
    print("\n" + "="*50)
    print("   ALGORITHM PARAMETERS")
    print("="*50)
    
    # Discount factor
    while True:
        try:
            gamma_input = input("\nEnter discount factor γ (0-1) [0.9]: ").strip()
            if not gamma_input:
                gamma = 0.9
            else:
                gamma = float(gamma_input)
            
            if gamma < 0 or gamma > 1:
                print("❌ Gamma must be between 0 and 1")
                continue
            
            print(f"✅ Gamma (γ): {gamma}")
            break
        except ValueError:
            print("❌ Invalid input. Please enter a number between 0 and 1.")
    
    # Convergence threshold
    while True:
        try:
            theta_input = input("Enter convergence threshold θ [0.001]: ").strip()
            if not theta_input:
                theta = 0.001
            else:
                theta = float(theta_input)
            
            if theta <= 0:
                print("❌ Theta must be positive")
                continue
            
            print(f"✅ Theta (θ): {theta}")
            break
        except ValueError:
            print("❌ Invalid input. Please enter a positive number.")
    
    # Max iterations
    while True:
        try:
            max_iter_input = input("Enter maximum iterations [100]: ").strip()
            if not max_iter_input:
                max_iterations = 100
            else:
                max_iterations = int(max_iter_input)
            
            if max_iterations < 1:
                print("❌ Must be at least 1 iteration")
                continue
            
            print(f"✅ Max iterations: {max_iterations}")
            break
        except ValueError:
            print("❌ Invalid input. Please enter a positive integer.")
    
    return gamma, theta, max_iterations

def get_user_configuration():
    """Main function to get all configuration from user"""
    print("\n" + "="*70)
    print("   VALUE ITERATION - INTERACTIVE SETUP")
    print("="*70)
    print("\nNote: Grid uses 0-based indexing")
    print("Example: For a 4x4 grid, states are from (0,0) to (3,3)")
    
    # Get grid dimensions
    rows, cols = get_grid_dimensions()
    
    # Get special states
    goal = get_goal_state(rows, cols)
    fire = get_fire_state(rows, cols, goal)
    obstacles = get_obstacles(rows, cols, goal, fire)
    start = get_start_state(rows, cols, goal, fire, obstacles)
    
    # Get algorithm parameters
    gamma, theta, max_iterations = get_algorithm_parameters()
    
    # Summary
    print("\n" + "="*70)
    print("   CONFIGURATION SUMMARY")
    print("="*70)
    print(f"Grid Size:        {rows}x{cols}")
    print(f"Goal State:       {goal} (reward: +1)")
    print(f"Fire State:       {fire if fire else 'None'} {('(reward: -1)' if fire else '')}")
    print(f"Obstacles:        {obstacles if obstacles else 'None'}")
    print(f"Start State:      {start if start else 'Not specified'}")
    print(f"Discount (γ):     {gamma}")
    print(f"Threshold (θ):    {theta}")
    print(f"Max Iterations:   {max_iterations}")
    print("="*70)
    
    response = input("\nProceed with this configuration? (yes/no) [yes]: ").strip().lower()
    if response in ['no', 'n']:
        print("\n❌ Configuration cancelled. Exiting...")
        return None
    
    return {
        'rows': rows,
        'cols': cols,
        'goal': goal,
        'fire': fire,
        'obstacles': obstacles,
        'start': start,
        'gamma': gamma,
        'theta': theta,
        'max_iterations': max_iterations
    }

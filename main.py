# main.py - Main Execution Script with Interactive Input

import config_dynamic
from input_handler import get_user_configuration
from environment import GridWorld
from value_iteration import ValueIteration
from visualizer import Visualizer
import matplotlib.pyplot as plt
import sys

def main():
    # Get configuration from user
    user_config = get_user_configuration()
    
    if user_config is None:
        sys.exit(0)
    
    # Set the configuration
    config_dynamic.set_configuration(user_config)
    
    print("\n" + "="*70)
    print("   RUNNING VALUE ITERATION")
    print("="*70)
    
    # Create environment
    env = GridWorld()
    print(f"\n✅ Environment created: {env.rows}x{env.cols} Grid")
    print(f"   Goal: {env.goal} | Fire: {env.fire} | Obstacles: {len(env.obstacles)}")
    
    # Run Value Iteration
    vi = ValueIteration(env)
    num_iterations = vi.run(max_iterations=user_config['max_iterations'])
    
    # Create visualizer
    viz = Visualizer(vi)
    
    # Print final results as text
    print("\n" + "="*70)
    print("   FINAL RESULTS")
    print("="*70)
    viz.print_text_grid()
    viz.print_policy()
    
    # Ask user what visualizations they want
    print("\n" + "="*70)
    print("   VISUALIZATION OPTIONS")
    print("="*70)
    print("\n1. Animation of all iterations")
    print("2. Final value function heatmap")
    print("3. Optimal policy with arrows")
    print("4. All of the above")
    print("5. Skip visualizations")
    
    while True:
        choice = input("\nSelect visualization (1-5) [4]: ").strip()
        if not choice:
            choice = '4'
        
        if choice in ['1', '2', '3', '4', '5']:
            break
        print("❌ Invalid choice. Please enter 1, 2, 3, 4, or 5")
    
    if choice == '5':
        print("\n✅ Skipping visualizations")
    else:
        print("\n📊 Generating visualizations...")
        
        if choice in ['1', '4']:
            print("   - Creating animation...")
            anim = viz.animate_iterations()
            plt.show()
        
        if choice in ['2', '4']:
            print("   - Creating value function plot...")
            fig1 = viz.plot_iteration(num_iterations - 1)
            plt.show()
        
        if choice in ['3', '4']:
            print("   - Creating policy plot...")
            fig2 = viz.plot_policy()
            plt.show()
    
    print("\n" + "="*70)
    print("   ✅ VALUE ITERATION COMPLETE!")
    print("="*70)
    print(f"\n📊 Summary:")
    print(f"   Total iterations: {num_iterations}")
    print(f"   Grid size: {env.rows}x{env.cols}")
    print(f"   States processed: {len(env.get_all_states())}")
    print(f"   Discount factor (γ): {user_config['gamma']}")
    print(f"   Convergence threshold (θ): {user_config['theta']}")
    print("\n   Thank you for using Value Iteration! 🎉\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Program interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

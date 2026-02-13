# visualizer.py - Visualization Module

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import numpy as np
import config_dynamic as config

class Visualizer:
    """Visualize Value Function and Policy"""
    
    def __init__(self, value_iteration):
        self.vi = value_iteration
        self.env = value_iteration.env
    
    def print_text_grid(self, iteration=None):
        """Print value function as text grid"""
        grid = self.vi.get_value_grid(iteration)
        
        print("\nValue Function:")
        print("─" * (self.env.cols * 8 + 1))
        for row in grid:
            print("│", end="")
            for val in row:
                print(f" {val:6.3f} │", end="")
            print()
            print("─" * (self.env.cols * 8 + 1))
    
    def print_policy(self):
        """Print optimal policy as text grid"""
        grid = self.vi.get_policy_grid()
        
        print("\nOptimal Policy:")
        print("─" * (self.env.cols * 4 + 1))
        for row in grid:
            print("│", end="")
            for cell in row:
                print(f" {cell:^2} │", end="")
            print()
            print("─" * (self.env.cols * 4 + 1))
    
    def plot_iteration(self, iteration):
        """Plot value function for a specific iteration"""
        grid = self.vi.get_value_grid(iteration)
        
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Plot heatmap
        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto', vmin=-1, vmax=1)
        
        # Add colorbar
        plt.colorbar(im, ax=ax, label='Value')
        
        # Add grid lines
        ax.set_xticks(np.arange(self.env.cols))
        ax.set_yticks(np.arange(self.env.rows))
        ax.set_xticks(np.arange(self.env.cols) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.env.rows) - 0.5, minor=True)
        ax.grid(which='minor', color='black', linewidth=2)
        
        # Add value text
        for i in range(self.env.rows):
            for j in range(self.env.cols):
                if (i, j) in self.env.obstacles:
                    ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1, 
                                          fill=True, color='gray', alpha=0.5))
                    text = ax.text(j, i, 'X', ha='center', va='center',
                                 color='black', fontsize=20, weight='bold')
                elif (i, j) == self.env.goal:
                    text = ax.text(j, i, f'G\n{grid[i][j]:.2f}', 
                                 ha='center', va='center', color='black', fontsize=12)
                elif self.env.fire and (i, j) == self.env.fire:
                    text = ax.text(j, i, f'F\n{grid[i][j]:.2f}', 
                                 ha='center', va='center', color='black', fontsize=12)
                else:
                    text = ax.text(j, i, f'{grid[i][j]:.2f}', 
                                 ha='center', va='center', color='black', fontsize=12)
        
        ax.set_title(f'Value Function - Iteration {iteration}', fontsize=16, weight='bold')
        ax.set_xlabel('Column', fontsize=12)
        ax.set_ylabel('Row', fontsize=12)
        
        plt.tight_layout()
        return fig
    
    def plot_policy(self):
        """Plot optimal policy with arrows"""
        grid = self.vi.get_value_grid()
        policy_grid = self.vi.get_policy_grid()
        
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Plot heatmap
        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto', vmin=-1, vmax=1)
        plt.colorbar(im, ax=ax, label='Value')
        
        # Add grid lines
        ax.set_xticks(np.arange(self.env.cols))
        ax.set_yticks(np.arange(self.env.rows))
        ax.set_xticks(np.arange(self.env.cols) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.env.rows) - 0.5, minor=True)
        ax.grid(which='minor', color='black', linewidth=2)
        
        # Add policy arrows and values
        for i in range(self.env.rows):
            for j in range(self.env.cols):
                if (i, j) in self.env.obstacles:
                    ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1, 
                                          fill=True, color='gray', alpha=0.5))
                    ax.text(j, i, 'X', ha='center', va='center',
                           color='black', fontsize=20, weight='bold')
                else:
                    # Add arrow
                    arrow = policy_grid[i][j]
                    ax.text(j, i-0.2, arrow, ha='center', va='center',
                           color='black', fontsize=24, weight='bold')
                    # Add value
                    ax.text(j, i+0.25, f'{grid[i][j]:.2f}', ha='center', va='center',
                           color='black', fontsize=10)
        
        ax.set_title('Optimal Policy', fontsize=16, weight='bold')
        ax.set_xlabel('Column', fontsize=12)
        ax.set_ylabel('Row', fontsize=12)
        
        plt.tight_layout()
        return fig
    
    def animate_iterations(self, save_path=None):
        """Create animation of value iteration convergence"""
        fig, ax = plt.subplots(figsize=(8, 8))
        
        def update(frame):
            ax.clear()
            grid = self.vi.get_value_grid(frame)
            
            # Plot heatmap
            im = ax.imshow(grid, cmap='RdYlGn', aspect='auto', vmin=-1, vmax=1)
            
            # Add grid lines
            ax.set_xticks(np.arange(self.env.cols))
            ax.set_yticks(np.arange(self.env.rows))
            ax.set_xticks(np.arange(self.env.cols) - 0.5, minor=True)
            ax.set_yticks(np.arange(self.env.rows) - 0.5, minor=True)
            ax.grid(which='minor', color='black', linewidth=2)
            
            # Add value text and special markers
            for i in range(self.env.rows):
                for j in range(self.env.cols):
                    if (i, j) in self.env.obstacles:
                        ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1, 
                                              fill=True, color='gray', alpha=0.5))
                        ax.text(j, i, 'X', ha='center', va='center',
                               color='black', fontsize=20, weight='bold')
                    elif (i, j) == self.env.goal:
                        ax.text(j, i, f'G\n{grid[i][j]:.2f}', 
                               ha='center', va='center', color='black', fontsize=12)
                    elif self.env.fire and (i, j) == self.env.fire:
                        ax.text(j, i, f'F\n{grid[i][j]:.2f}', 
                               ha='center', va='center', color='black', fontsize=12)
                    else:
                        ax.text(j, i, f'{grid[i][j]:.2f}', 
                               ha='center', va='center', color='black', fontsize=12)
            
            ax.set_title(f'Value Iteration - Iteration {frame}', fontsize=16, weight='bold')
            ax.set_xlabel('Column', fontsize=12)
            ax.set_ylabel('Row', fontsize=12)
            
            return ax,
        
        anim = animation.FuncAnimation(fig, update, frames=len(self.vi.history),
                                      interval=500, repeat=True, blit=False)
        
        if save_path:
            anim.save(save_path, writer='pillow', fps=2)
            print(f"\nAnimation saved to {save_path}")
        
        plt.tight_layout()
        return anim
    
    def show_all_iterations(self):
        """Show each iteration as separate plot"""
        num_iterations = len(self.vi.history)
        
        for i in range(num_iterations):
            fig = self.plot_iteration(i)
            plt.show()
            plt.close()

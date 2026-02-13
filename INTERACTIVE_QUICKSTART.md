# 🚀 INTERACTIVE VALUE ITERATION - QUICK START

## ✅ What's New - Interactive Setup!

Now you can **configure everything interactively**:
- ✅ Grid dimensions (user input!)
- ✅ Goal state position
- ✅ Fire state (optional)
- ✅ Obstacles (as many as you want)
- ✅ Start state (optional, for visualization)
- ✅ Algorithm parameters (γ, θ, max iterations)

**No more editing config files!** Just run and answer questions.

---

## 📦 Files Overview

| File | Purpose | New? |
|------|---------|------|
| **input_handler.py** | Interactive user input | ✅ NEW |
| **config_dynamic.py** | Dynamic configuration | ✅ NEW |
| **config.py** | Static config (backup) | Old |
| **environment.py** | Grid world logic | Updated |
| **value_iteration.py** | Core algorithm | Updated |
| **visualizer.py** | Plots and animations | Updated |
| **main.py** | Interactive runner | ✅ NEW |

---

## 🎯 How to Run

### Step 1: Install dependencies
```bash
pip install matplotlib numpy
```

### Step 2: Run the program
```bash
python main.py
```

### Step 3: Answer the questions!

---

## 📝 Example Session

```
======================================================================
   VALUE ITERATION - INTERACTIVE SETUP
======================================================================

Note: Grid uses 0-based indexing
Example: For a 4x4 grid, states are from (0,0) to (3,3)

==================================================
   GRID SETUP
==================================================

Enter grid dimensions (rows cols): 4 4
✅ Grid size: 4x4

📍 Goal State (reward: +1)
Enter goal state (row col): 0 3
✅ Goal: (0, 3)

🔥 Fire State (reward: -1) [Optional]
Do you want a fire state? (yes/no) [no]: yes
Enter fire state (row col): 1 3
✅ Fire: (1, 3)

🚧 Obstacles [Optional]
Do you want obstacles? (yes/no) [no]: yes
Enter obstacles one by one. Press Enter without input when done.
Obstacle 1 (row col) or [Enter to finish]: 1 1
✅ Obstacle 1 added: (1, 1)
Obstacle 2 (row col) or [Enter to finish]: 
✅ Total obstacles: 1

🎯 Start State [Optional]
Do you want to specify a start state? (yes/no) [no]: yes
Enter start state (row col): 3 0
✅ Start: (3, 0)

==================================================
   ALGORITHM PARAMETERS
==================================================

Enter discount factor γ (0-1) [0.9]: 0.9
✅ Gamma (γ): 0.9
Enter convergence threshold θ [0.001]: 0.001
✅ Theta (θ): 0.001
Enter maximum iterations [100]: 50
✅ Max iterations: 50

======================================================================
   CONFIGURATION SUMMARY
======================================================================
Grid Size:        4x4
Goal State:       (0, 3) (reward: +1)
Fire State:       (1, 3) (reward: -1)
Obstacles:        [(1, 1)]
Start State:      (3, 0)
Discount (γ):     0.9
Threshold (θ):    0.001
Max Iterations:   50
======================================================================

Proceed with this configuration? (yes/no) [yes]: yes

======================================================================
   RUNNING VALUE ITERATION
======================================================================

✅ Environment created: 4x4 Grid
   Goal: (0, 3) | Fire: (1, 3) | Obstacles: 1

--- Value Iteration Started ---

Iteration 1: max_change = 1.000000
Iteration 2: max_change = 0.900000
Iteration 3: max_change = 0.810000
Iteration 4: max_change = 0.729000
Iteration 5: max_change = 0.656100
Iteration 6: max_change = 0.590490
Iteration 7: max_change = 0.000000

✅ Converged after 7 iterations!
   (Convergence threshold θ = 0.001)

📊 Total iterations completed: 7

======================================================================
   FINAL RESULTS
======================================================================

Value Function:
─────────────────────────────────
│  0.810 │  0.900 │  1.000 │  0.000 │
─────────────────────────────────
│  0.729 │  0.000 │  0.900 │  0.000 │
─────────────────────────────────
│  0.656 │  0.729 │  0.810 │  0.729 │
─────────────────────────────────
│  0.590 │  0.656 │  0.729 │  0.656 │
─────────────────────────────────

Optimal Policy:
─────────────────
│ →  │ →  │ →  │ G  │
─────────────────
│ ↑  │ X  │ ↑  │ F  │
─────────────────
│ ↑  │ →  │ ↑  │ ←  │
─────────────────
│ ↑  │ ↑  │ ↑  │ ↑  │
─────────────────

======================================================================
   VISUALIZATION OPTIONS
======================================================================

1. Animation of all iterations
2. Final value function heatmap
3. Optimal policy with arrows
4. All of the above
5. Skip visualizations

Select visualization (1-5) [4]: 4

📊 Generating visualizations...
   - Creating animation...
   - Creating value function plot...
   - Creating policy plot...

======================================================================
   ✅ VALUE ITERATION COMPLETE!
======================================================================

📊 Summary:
   Total iterations: 7
   Grid size: 4x4
   States processed: 15
   Discount factor (γ): 0.9
   Convergence threshold (θ): 0.001

   Thank you for using Value Iteration! 🎉
```

---

## ⚙️ Input Guide

### Grid Dimensions
```
Enter grid dimensions (rows cols): 5 5
```
- Minimum: 2x2
- Maximum: 20x20

### Goal State
```
Enter goal state (row col): 0 4
```
- Required
- Must be within grid bounds
- Receives reward of +1

### Fire State
```
Do you want a fire state? (yes/no) [no]: yes
Enter fire state (row col): 2 4
```
- Optional
- Receives reward of -1
- Cannot be same as goal

### Obstacles
```
Do you want obstacles? (yes/no) [no]: yes
Obstacle 1 (row col) or [Enter to finish]: 1 1
Obstacle 2 (row col) or [Enter to finish]: 2 2
Obstacle 3 (row col) or [Enter to finish]: 
```
- Optional
- Add as many as you want
- Cannot overlap with goal/fire
- Press Enter alone to finish

### Start State
```
Do you want to specify a start state? (yes/no) [no]: yes
Enter start state (row col): 4 0
```
- Optional
- Only used for visualization/understanding
- Algorithm finds optimal policy for ALL states

### Algorithm Parameters

**Discount Factor (γ):**
```
Enter discount factor γ (0-1) [0.9]: 0.95
```
- Range: 0 to 1
- Higher = more far-sighted
- Default: 0.9

**Convergence Threshold (θ):**
```
Enter convergence threshold θ [0.001]: 0.0001
```
- Smaller = more precise
- Larger = faster convergence
- Default: 0.001

**Maximum Iterations:**
```
Enter maximum iterations [100]: 200
```
- Safety limit to prevent infinite loops
- Algorithm stops early if converged
- Default: 100

---

## 🎨 Visualization Options

After algorithm runs, choose what to see:

1. **Animation** - Watch values converge iteration by iteration
2. **Final heatmap** - See final value function as colored grid
3. **Policy arrows** - See optimal actions with arrows (↑↓←→)
4. **All of the above** - Show everything (recommended!)
5. **Skip** - Just see text output

---

## 💡 Quick Examples

### Example 1: Small Grid
```
Dimensions: 3 3
Goal: 0 2
Fire: no
Obstacles: no
Start: 2 0
γ: 0.9
θ: 0.001
Max iterations: 50
```

### Example 2: Maze-like Grid
```
Dimensions: 5 5
Goal: 0 4
Fire: yes → 2 4
Obstacles: yes → (1,1), (1,2), (2,2), (3,2)
Start: 4 0
γ: 0.9
θ: 0.001
Max iterations: 100
```

### Example 3: Large Grid
```
Dimensions: 10 10
Goal: 0 9
Fire: yes → 5 9
Obstacles: yes → add a few scattered
Start: 9 0
γ: 0.95
θ: 0.0001
Max iterations: 200
```

---

## 🔧 Understanding Start State

**Important:** The start state is **optional** and only affects visualization.

- **What it does:** Shows you where an agent might begin
- **What it doesn't do:** Doesn't change the algorithm
- **Why?** Value Iteration finds the optimal policy for **ALL states**, not just one

**In the animation:** If you specify a start state, it helps you trace the path from start to goal.

---

## 📊 Understanding the Output

### Iteration Count
```
Iteration 1: max_change = 1.000000
Iteration 2: max_change = 0.900000
...
Iteration 7: max_change = 0.000000

✅ Converged after 7 iterations!
📊 Total iterations completed: 7
```

Shows how values changed each iteration and when convergence happened.

### Value Function
```
│  0.810 │  0.900 │  1.000 │  0.000 │
```
- Higher values = better states
- Goal state: always shows final reward
- Fire state: always shows penalty

### Policy Grid
```
│ →  │ →  │ →  │ G  │
│ ↑  │ X  │ ↑  │ F  │
```
- Arrows (↑↓←→) = optimal action
- G = Goal
- F = Fire
- X = Obstacle

---

## 🐛 Troubleshooting

### "Out of bounds" error
- Check your grid size
- State indices start at 0
- For 4x4 grid: valid states are (0,0) to (3,3)

### Values not converging
- Increase max_iterations
- Check that goal is reachable
- Try larger θ for faster (less precise) convergence

### No visualization showing
- Make sure matplotlib is installed
- Try option 5 (skip) to see text only
- Check for errors in console

---

## 🎓 Learning Tips

1. **Start simple:** Try 3x3 grid first
2. **Watch convergence:** See how values propagate from goal
3. **Experiment with γ:** See how it affects policy
4. **Add obstacles:** See how policy routes around them
5. **Compare iterations:** Watch the animation carefully

---

## 🚀 Next Steps

After mastering interactive setup:

1. Try different grid sizes
2. Experiment with γ values
3. Create complex mazes with obstacles
4. Compare convergence speeds
5. Implement Policy Iteration next!

---

## 📝 Key Features

✅ **Fully interactive** - No file editing needed  
✅ **Error handling** - Validates all inputs  
✅ **Flexible** - Fire and obstacles are optional  
✅ **User-friendly** - Clear prompts and defaults  
✅ **Iteration tracking** - Shows convergence progress  
✅ **Multiple visualizations** - Choose what you want to see  

---

**Perfect for your practical! Professional, interactive, and easy to demonstrate! 🎉**

Run `python main.py` and enjoy! 🚀

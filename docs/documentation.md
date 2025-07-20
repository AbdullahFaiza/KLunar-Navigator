Khadijah’s Lunar (K-Lunar) Navigator Documentation

Overview
This project, named Khadijah’s Lunar Navigator in honor of my daughter, implements a lunar rover path planning AI using Q-learning, a reinforcement learning algorithm. The rover navigates a grid-based lunar terrain, avoiding craters (obstacles) to reach a target while minimizing energy consumption. The simulation is visualized using Pygame for an engaging user experience on a 10x10 lunar grid. The rover (blue square) learns to move from (0,0) to (9,9) (green square) while avoiding obstacles (red circles).

Implementation Details
- **Environment**: Managed by `environment.py`, a 10x10 grid with a start position (0,0), target (9,9), and random obstacles.
- **Rover**: Controlled by `rover.py`, moves based on four actions (right, left, down, up) with energy tracking.
- **Q-Learning Agent**: Implemented in `q_learning.py`, uses a Q-table to learn optimal paths with adjustable learning rate, discount factor, and epsilon.
- **Visualization**: Handled by `visualizer.py`, renders the grid, rover, target, and obstacles in a 600x600 Pygame window.

Code Structure
main.py: Orchestrates the simulation, integrating environment, rover, agent, and visualizer.
rover.py: Manages rover movement and position validation.
environment.py: Defines the lunar terrain, obstacles, and rewards.
q_learning.py: Implements the Q-learning algorithm with Q-table management.
visualizer.py: Renders the simulation using Pygame.

Development and Fixes
The following updates were made to resolve issues during development:

- Added `from rover import Rover` to `environment.py` to fix the "Rover not defined" error.
- Fixed state synchronization by ensuring `env.rover_pos` matches `rover.position` across `environment.py`, `rover.py`, and `main.py`.
- Reduced obstacle count from `size * 2` to `size // 3` (3 for 10x10 grid) in `environment.py` to prevent early blocking (e.g., at (1,0)).
- Increased `learning_rate` from 0.1 to 0.4 and `discount_factor` from 0.9 to 0.98 in `q_learning.py` for faster Q-table convergence.
- Adjusted `epsilon` from 0.05 to 0.15 in `q_learning.py` for balanced exploration.
- Added `max_steps = 200` in `main.py` to cap each episode and prevent infinite loops.
- Enhanced debug prints across all files to track `rover_pos`, `state`, `action`, and `done` status, though terminal output was not shown (possible buffering issue).

- **Verification**:
  - Confirmed blue rover moves from (0,0) toward (9,9) with visual feedback.
  - Expected behavior: Episodes 1/100 to 100/100 logged, `q_table.npy` generated after 100 episodes.

Known Issues and Workarounds
- **Debug Output Missing**: Terminal logs were not displayed, possibly due to buffering. Consider adding `sys.stdout.flush()` after prints if debugging is needed (e.g., `print("message"); sys.stdout.flush()`).
- **Obstacle Impact**: If movement stalls, manually set `obstacles = set()` in `environment.py`’s `__init__` to test without obstacles.

Future Improvements
- Add reward visualization (e.g., a chart of episode rewards).
- Implement dynamic obstacle generation based on rover progress.
- Optimize Q-learning parameters based on final performance.

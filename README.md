# Khadijah’s Lunar (K-Lunar) Navigator
## Author: Faiza Abdullah
### Project Track: Implementation Track
Description: This project implements an AI-powered lunar rover path planning system, named in honor of my daughter Khadijah, using reinforcement learning (Q-learning) to navigate a simulated lunar terrain. The rover optimizes its path to reach a target while avoiding craters and minimizing energy consumption. The simulation is visualized using Pygame, and the codebase is modular, well-documented, and includes error handling.

**How to Run the Code**

Prerequisites
- Python 3.8+
- Install dependencies: pip install -r requirements.txt
- Ensure Git is installed for repository cloning

Setup Instructions
- Clone the repository:

git clone https://github.com/AbdullahFaiza/KLunar-Navigator.git

cd KLunar-navigator

- Install dependencies:

pip install -r requirements.txt

- Run the main script:

python main.py

**Running the Simulation**
- The simulation launches a Pygame window displaying the lunar terrain (grid-based).
- The rover (blue square) navigates toward the target (green star), avoiding craters (red circles).
- Press R to reset the simulation, Q to quit.
- The console outputs the rover’s current position, energy used, and episode statistics.

**Project Structure**
- main.py: Entry point, initializes Pygame and runs the simulation.
- rover.py: Defines the Rover class with movement and Q-learning logic.
- environment.py: Defines the lunar terrain, obstacles, and rewards.
- q_learning.py: Implements the Q-learning algorithm.
- visualizer.py: Handles Pygame visualization.
- requirements.txt: Lists dependencies (pygame, numpy)
- docs/: Contains detailed documentation (see docs/documentation.md).
- slides/: Contains presentation slides (see slides/presentation.pdf).

**Notes**
- The code includes error handling for invalid inputs, file loading, and simulation crashes.
- The Q-learning model saves its Q-table to q_table.npy for persistence.
- See docs/documentation.md for detailed code explanations and algorithm overview.

### Conceptual Track Submissions within Implementation track as additional part

This project extends to the Conceptual Track, proposing innovative enhancements and planning for future development. The following artifacts are included:

**Project Proposal**
- Location: docs/project_proposal.md
- Details: Outlines the goal of simulating lunar rover navigation with Q-learning, targeting educational and research applications. Proposes scalability and robustness as key objectives.

**Detailed Solution Plan**
- Location: docs/solution_plan.md
- Details: Describes the architecture (Environment, Rover, Q-Learning, Visualization) and technical optimizations (state sync, reduced obstacles, adjusted learning parameters).

**Testing Plan**
- Location: docs/testing_plan.md
- Details: Defines test cases for movement, obstacle avoidance, target reach, boundary checks, and episode completion. Targets 100 episodes with a 20,000-step limit.

**Presentation Slides**
- Location: presentations/presentation_slides.pdf
- Details: A PDF slide deck summarizing the project, including an introduction, solution overview, technical highlights, testing results, and conclusion. Includes the creative angle and also snapshot and a quick video of resultant of moving rover.

**Creative Addition: KLunar Navigator Mascot & Architecture**
- Concept: A cheerful Klunar navigator, depicted as a blue robotic rover with an astronaut helmet featuring a glowing visor map. Represents the rover’s journey and resilience.
- Purpose: Enhances engagement in presentations and documentation.
- Narrative: “KLunar Navigator explores the lunar plains, learning to avoid craters and reach its base!”

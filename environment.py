from rover import Rover
import random

class LunarEnvironment:
    def __init__(self, size):
        self.size = size
        self.start_pos = (0, 0)
        self.target_pos = (size - 1, size - 1)
        self.obstacles = self._generate_obstacles()
        self.rover_pos = self.start_pos
        print(f"Initialized - Target: {self.target_pos}, Obstacles: {self.obstacles}")  # Debug

    def _generate_obstacles(self):
        obstacles = set()
        num_obstacles = self.size // 3  # Further reduced to 3 for 10x10 grid
        while len(obstacles) < num_obstacles:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) != self.start_pos and (x, y) != self.target_pos and (x, y) != (1, 0):  # Avoid early block
                obstacles.add((x, y))
        return obstacles

    def reset(self):
        self.rover_pos = self.start_pos
        print(f"Reset to {self.rover_pos}")  # Debug
        return self.rover_pos

    def step(self, action_idx):
        try:
            rover = Rover(self)
            rover.position = self.rover_pos  # Sync rover with environment
            new_pos = rover.move(action_idx)
            self.rover_pos = new_pos  # Update environment position
            print(f"Step - Rover Pos: {self.rover_pos}, New Pos: {new_pos}")  # Debug
            reward = -1  # Base movement cost
            done = False
            if self.rover_pos == self.target_pos:
                reward = 100
                done = True
                print(f"Reached target at {self.rover_pos}")
            elif self.rover_pos in self.obstacles:
                reward = -50
                done = True
                print(f"Hit obstacle at {self.rover_pos}")
            return self.rover_pos, reward, done
        except Exception as e:
            print(f"Environment step error: {e}")
            return self.rover_pos, -10, False
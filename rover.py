class Rover:
    def __init__(self, env):
        self.env = env
        self.position = env.rover_pos  # Start with environment's position
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        self.energy = 0

    def move(self, action_idx):
        try:
            dx, dy = self.actions[action_idx]
            new_x = self.position[0] + dx
            new_y = self.position[1] + dy
            if 0 <= new_x < self.env.size and 0 <= new_y < self.env.size:
                new_pos = (new_x, new_y)
                if new_pos not in self.env.obstacles:
                    self.position = new_pos
                    self.energy += 1
                    print(f"Moving to {new_pos} with action {action_idx}")
                else:
                    print(f"Hit obstacle at {new_pos}, staying at {self.position}")
            else:
                print(f"Out of bounds at {new_x}, {new_y}, staying at {self.position}")
            return self.position
        except IndexError:
            print(f"Invalid action index {action_idx}, staying at {self.position}")
            return self.position
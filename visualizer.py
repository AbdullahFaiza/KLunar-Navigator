import pygame

class Visualizer:
    def __init__(self, env):
        self.env = env
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("KLunar Rover Path Learning")
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill((150, 150, 150))  # Gray background
        cell_size = 600 // self.env.size
        for x in range(self.env.size):
            for y in range(self.env.size):
                pygame.draw.rect(self.screen, (255, 255, 255), (y * cell_size, x * cell_size, cell_size - 1, cell_size - 1), 1)
        pygame.draw.rect(self.screen, (0, 255, 0), (self.env.target_pos[1] * cell_size, self.env.target_pos[0] * cell_size, cell_size, cell_size))
        for obs in self.env.obstacles:
            pygame.draw.circle(self.screen, (255, 0, 0), (obs[1] * cell_size + cell_size // 2, obs[0] * cell_size + cell_size // 2), cell_size // 3)
        pygame.display.flip()

    def update(self, pos):
        self.screen.fill((150, 150, 150))
        self.draw()
        cell_size = 600 // self.env.size
        pygame.draw.rect(self.screen, (0, 0, 255), (pos[1] * cell_size, pos[0] * cell_size, cell_size, cell_size))  # Blue rover
        pygame.display.flip()
        self.clock.tick(60)
        print(f"Visualizing at {pos}")  # Debug
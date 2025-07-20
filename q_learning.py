import numpy as np

class QLearningAgent:
    def __init__(self, env):
        self.env = env
        self.q_table = np.zeros((self.env.size, self.env.size, 4))  # 4 actions
        self.learning_rate = 0.4  # Increased for faster learning
        self.discount_factor = 0.98  # Increased for stronger future reward focus
        self.epsilon = 0.15  # Adjusted for balanced exploration
        self.energy = 0

    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.randint(4)
        else:
            return np.argmax(self.q_table[state[0], state[1]])

    def learn(self, state, action, reward, next_state, done):
        best_next_action = np.max(self.q_table[next_state[0], next_state[1]])
        td_target = reward + self.discount_factor * best_next_action * (1 - done)
        td_error = td_target - self.q_table[state[0], state[1], action]
        self.q_table[state[0], state[1], action] += self.learning_rate * td_error
        self.energy += 1

    def save_q_table(self):
        np.save('q_table.npy', self.q_table)
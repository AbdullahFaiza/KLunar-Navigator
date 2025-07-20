import pygame
import sys
import numpy as np
from rover import Rover
from environment import LunarEnvironment
from q_learning import QLearningAgent
from visualizer import Visualizer
import asyncio
import platform

FPS = 60

def setup():
    global env, agent, visualizer
    pygame.init()
    env = LunarEnvironment(10)
    agent = QLearningAgent(env)
    visualizer = Visualizer(env)
    visualizer.draw()

async def update_loop():
    global env, agent, visualizer
    state = env.rover_pos
    action = agent.choose_action(state)
    next_state, reward, done = env.step(action)
    agent.learn(state, action, reward, next_state, done)
    visualizer.update(next_state)
    env.rover_pos = next_state  # Force sync
    await asyncio.sleep(1.0 / FPS)
    print(f"State: {state}, Action: {action}, Next: {next_state}, Reward: {reward}, Done: {done}, Rover Pos: {env.rover_pos}")  # Enhanced debug
    sys.stdout.flush()
    return done, reward

async def main():
    setup()
    for episode in range(100):
        state = env.reset()
        done = False
        episode_reward = 0
        steps = 0
        max_steps = 200  # Increased to allow more exploration
        while not done and steps < max_steps:
            done, reward = await update_loop()
            episode_reward += reward
            steps += 1
            if steps % 10 == 0:  # Periodic check
                print(f"Episode {episode + 1} Step {steps}, Current Pos: {env.rover_pos}")
        print(f"Episode {episode + 1}/100, Total Reward: {episode_reward}, Energy: {agent.energy}, Steps: {steps}")
    agent.save_q_table()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
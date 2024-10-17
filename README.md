# arcade-pong
# Pong Game

## Overview

This project is a **Pong Game** built using Python's `turtle` module. Pong is a two-player arcade game where players control paddles to prevent a ball from passing their side of the screen. The game keeps track of the score for both players, and players can move their paddles up and down to block the ball.

## Features

- **Paddle Movement**: Each player controls a paddle using keyboard inputs.
- **Ball Movement**: The ball moves across the screen and bounces off the walls and paddles.
- **Score Tracking**: The game tracks the score for both players. A point is awarded to a player when the opponent misses the ball.

## Controls

- **Right Paddle**:
  - `Up Arrow`: Move the paddle up
  - `Down Arrow`: Move the paddle down
- **Left Paddle**:
  - `W`: Move the paddle up
  - `S`: Move the paddle down

## How to Run the Game

1. Make sure you have Python installed on your computer.
2. Clone or download this repository to your local machine.
3. Navigate to the folder where the game is saved.
4. Run the game by executing:
   ```bash
   python main.py
   ```

## Project Structure

- **`main.py`**: The main game loop and control logic.
- **`paddle.py`**: The `Paddle` class manages paddle creation and movement.
- **`ball.py`**: The `Ball` class handles the movement and bouncing of the ball.
- **`scoreboard.py`**: The `Scoreboard` class tracks and displays the score.

## Dependencies

- Python 3.x (including the `turtle` module, which comes pre-installed with Python).

## How the Game Works

1. **Paddles**: Two paddles are positioned on the left and right sides of the screen. Players control them to block the ball.
2. **Ball Movement**: The ball starts at the center and moves diagonally. It bounces off the top and bottom walls and the paddles.
3. **Collision Detection**:
   - **Wall Collision**: If the ball hits the top or bottom of the screen, it bounces back in the opposite direction.
   - **Paddle Collision**: When the ball hits a paddle, it bounces back toward the other player.
4. **Scoring**: When the ball passes a paddle (i.e., goes beyond the left or right screen boundaries), a point is awarded to the opposing player, and the ball is reset to the center.

   
<img width="789" alt="pong-game" src="https://github.com/user-attachments/assets/a0ebaa81-b551-4e74-b849-c11accb737b9">


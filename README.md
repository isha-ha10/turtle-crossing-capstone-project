# Turtle Crossing Game 🐢🚗

## Overview

**Turtle Crossing** is a simple arcade-style game built with Python using the `turtle` graphics library. The objective of the game is to help the turtle safely cross a busy road filled with moving cars. Each time the turtle reaches the other side, the level increases and the cars move faster, making the game progressively more challenging.

This project demonstrates core **Python object-oriented programming concepts** such as classes, inheritance, lists of objects, and modular code structure.

---

## Features

* Player-controlled turtle
* Randomly generated cars
* Increasing difficulty with each level
* Collision detection system
* Scoreboard showing current level
* Game over screen when the turtle gets hit

---

## Controls

| Key          | Action                  |
| ------------ | ----------------------- |
| **Up Arrow** | Move the turtle forward |

---

## Game Rules

1. The turtle starts at the bottom of the screen.
2. Cars move from right to left across the road.
3. The player must guide the turtle to the top of the screen.
4. Each successful crossing increases the level.
5. Cars move faster as levels increase.
6. If a car hits the turtle, the game ends.

---

## Project Structure

```
turtle-crossing/
│
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
└── README.md
```

### main.py

Controls the main game loop and manages interactions between the player, cars, and scoreboard.

### player.py

Defines the **Player** class that controls the turtle character.

### car_manager.py

Handles creation, storage, and movement of all car objects.

### scoreboard.py

Displays the current level and the game-over message.

---

## Concepts Used

* Python Classes and Objects
* Inheritance
* Lists for managing multiple objects
* Event listeners
* Collision detection
* Game loops
* Modular project structure

---

## Requirements

* Python 3.x
* `turtle` module (comes pre-installed with Python)

---

## How to Run

1. Clone or download the repository.
2. Navigate to the project folder.
3. Run the game:

```bash
python main.py
```

---

## Future Improvements

Possible enhancements for the game:

* Add left and right movement
* Add sound effects
* Introduce different car speeds
* Add a start/restart screen
* Implement lane-based traffic

---


# Snake_Game_Using_Hand_Gesture_Recognition

A real-time hand gesture-controlled snake game using computer vision and hand tracking. This interactive project uses a webcam to detect the player's **index finger** and lets them control the snake without a keyboard or mouse. The game is built with **OpenCV**, **cvzone**, and **Python**, offering a modern, fun way to experience a classic game.

---

## Features

- **Real-Time Hand Tracking**:- Control the snake using your index finger with webcam input.

- **Dynamic Gameplay**:- Eat donuts to grow the snake and increase your score.

- **Collision Detection**:- Ends the game if the snake runs into itself.

- **Smooth Movement**:- Uses exponential smoothing for fluid hand motion.

- **Restart and Quit Options**:- Press keys to reset or quit the game.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- Webcam (for real-time tracking)

### Install Required Libraries

Use the command below to install all required Python libraries:

```bash
pip install -r requirements.txt
```

---

## Clone the Repository

```bash
git clone https://github.com/manish2kumar/Snake_Game_Using_Hand_Gesture_Recognition
cd Snake_Game_Using_Hand_Gesture_Recognition
```

---

## Technologies Used

- **OpenCV**: For capturing webcam feed and rendering visuals.
- **cvzone**: For hand detection and finger tracking.
- **NumPy**: For calculations like distance, array handling, etc.
- **Python**: Main programming language used to build the game.

---

## How to Use

### 1. Run the Game

Make sure `Donut.png` is placed in the same directory as your `snake_game.py` file.

```bash
python snake_game.py
```

### 2. Controls

| Key | Action       |
|-----|--------------|
| `r` | Restart Game |
| `q` | Quit Game    |

- Use your **index finger** (tracked via webcam) to control the snake’s direction.  
- Eat the donut to score and grow longer.  
- Don’t let the snake crash into itself — or it’s game over!

---

## Gameplay Preview

| Gameplay              | Snake Eats Donut        | Game Over               |
|-----------------------|-------------------------|-------------------------|
| ![Snake Moving](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2hnYTNhbGlubmd3c3YydzR0MGpwc3d3em52aGNza3VjdjRzdHQxZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7zYtI2HEGqVX8Zxah0/giphy.gif) | ![Eating Donut](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3drMjk1cjYzNnhpYjdlbGhweWYyMmptcjFzcWx2NGpyNDg1bzVzaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WoLX9jnBXbR5yMGF2m/giphy.gif) | ![Game Over](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd25vZ2VneXp3Ymo2Z3hoOGlnZzJoMHdrN3Z0eXp3aDltcmt2NXIzdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Hqtw4vzrni8cU/giphy.gif) |



---

## Contributors
- Manish Kumar - [GitHub Profile](https://github.com/manish2kumar)
- Ayush Kaushal - [GitHub Profile]( https://github.com/Ayushkaushal13)

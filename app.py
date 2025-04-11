import cvzone
import cv2
import numpy as np
import math
import random
from cvzone.HandTrackingModule import HandDetector

# Setup OpenCV capture and window size
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

detect = HandDetector(detectionCon=0.8, maxHands=1)


class SnakeGame:
    def __init__(self, foodPath):  # Fixed constructor name
        self.points = []  # Points of the snake
        self.lengths = []  # Distance between points
        self.currentLength = 0  # Total snake length
        self.maxLength = 150  # Maximum allowed length
        self.previousHead = (0, 0)  # Previous head position

        # Movement smoothing variables
        self.smoothFactor = 0.2  # Exponential Moving Average smoothing factor
        self.filteredHead = (0, 0)  # Smoothed head position

        # Food initialization
        self.foodIMG = cv2.imread(foodPath, cv2.IMREAD_UNCHANGED)
        self.foodHeight, self.foodWidth, _ = self.foodIMG.shape
        self.foodLocation = (0, 0)
        self.spawn_food()

        self.score = 0
        self.gameOver = False

    def spawn_food(self):
        self.foodLocation = (random.randint(100, 1180), random.randint(100, 620))

    def smooth_movement(self, newHead):
        if self.filteredHead == (0, 0):
            self.filteredHead = newHead  # Initialize on first frame
        else:
            # Apply Exponential Moving Average for smoothing
            self.filteredHead = (
                int(self.smoothFactor * newHead[0] + (1 - self.smoothFactor) * self.filteredHead[0]),
                int(self.smoothFactor * newHead[1] + (1 - self.smoothFactor) * self.filteredHead[1])
            )
        return self.filteredHead

    def update(self, frame, headCurrent):
        if self.gameOver:
            cvzone.putTextRect(frame, "Game Over", [250, 350], scale=8, thickness=4, colorT=(255, 255, 255),
                               colorR=(0, 0, 255), offset=20)
            cvzone.putTextRect(frame, f'Score: {self.score}', [250, 500], scale=8, thickness=5,
                               colorT=(255, 255, 255), colorR=(0, 0, 255), offset=20)
        else:
            headCurrent = self.smooth_movement(headCurrent)  # Apply movement smoothing
            prevX, prevY = self.previousHead
            currX, currY = headCurrent

            self.points.append([currX, currY])
            distance = math.hypot(currX - prevX, currY - prevY)
            self.lengths.append(distance)
            self.currentLength += distance
            self.previousHead = (currX, currY)

            # Limit snake length
            while self.currentLength > self.maxLength:
                self.currentLength -= self.lengths.pop(0)
                self.points.pop(0)

            # Check if snake eats food
            foodX, foodY = self.foodLocation
            if (foodX - self.foodWidth // 2 < currX < foodX + self.foodWidth // 2 and
                    foodY - self.foodHeight // 2 < currY < foodY + self.foodHeight // 2):
                self.spawn_food()
                self.maxLength += 50
                self.score += 1
                print("Score:", self.score)

            # Draw the snake
            if len(self.points) > 1:
                for i in range(1, len(self.points)):
                    cv2.line(frame, tuple(self.points[i - 1]), tuple(self.points[i]), (0, 0, 255), 20)
                cv2.circle(frame, tuple(self.points[-1]), 20, (200, 0, 200), cv2.FILLED)

            # Check self-collision
            if len(self.points) >= 3:
                pts = np.array(self.points[:-2], np.int32).reshape((-1, 1, 2))
                minDist = cv2.pointPolygonTest(pts, (currX, currY), True)
                if -1 <= minDist <= 1:
                    print("Collision detected!")
                    self.gameOver = True
                    self.reset()

            # Overlay food image
            frame = cvzone.overlayPNG(frame, self.foodIMG, (foodX - self.foodWidth // 2, foodY - self.foodHeight // 2))

            # Display score
            cvzone.putTextRect(frame, f'Score: {self.score}', [50, 80], scale=3, thickness=3, offset=10)

        return frame

    def reset(self):
        self.points.clear()
        self.lengths.clear()
        self.currentLength = 0
        self.maxLength = 150
        self.previousHead = (0, 0)
        self.filteredHead = (0, 0)
        self.spawn_food()
        self.score = 0
        self.gameOver = False


# Initialize game
game = SnakeGame("Donut.png")  # Ensure Donut.png exists in your project directory

while True:
    success, img = capture.read()
    img = cv2.flip(img, 1)
    hands, img = detect.findHands(img, flipType=False)

    if hands:
        landmarkList = hands[0]['lmList']
        indexFinger = tuple(landmarkList[8][0:2])
        img = game.update(img, indexFinger)

    cv2.imshow("Snake Game", img)
    key = cv2.waitKey(1)

    if key == ord('r'):
        game.reset()
    elif key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()


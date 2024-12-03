
# Enumeration for SignalType
from enum import Enum

class SignalType(Enum):
    GLIMMER = "Glimmer"
    BREEZE = "Breeze"
    STENCH = "Stench"
    GOLD = "Gold"
    NONE = "None"

# Point class to represent a square in the grid
class Point:
    def __init__(self, row: int, col: int, safe: bool = False, confirmed: bool = False, gold: bool = False):
        self.row = row
        self.col = col
        self.safe = safe
        self.confirmed = confirmed
        self.gold = gold

    def __repr__(self):
        return f"Point(row={self.row}, col={self.col}, safe={self.safe}, confirmed={self.confirmed}, gold={self.gold})"

# Signal class to represent the signal received from a square
class Signal:
    def __init__(self, point: Point, signal_type: SignalType):
        self.point = point
        self.signal_type = signal_type

    def __repr__(self):
        return f"Signal(point={self.point}, signal_type={self.signal_type.name})"

# Robot class to manage the robot's state and actions hopefully this is correct????????????????????????????????????????????
class Robot:
    def __init__(self, start_row: int, start_col: int):
        self.current_location = Point(start_row, start_col)
        self.orientation = 0  # 0: up, 1: right, 2: down, 3: left
        self.has_gold = False
        self.wumpus_dead = False
        self.wumpus_location = None  # Will be a Point when discovered

    def move(self, direction: str):
        if direction == "up":
            self.current_location.row -= 1
        elif direction == "down":
            self.current_location.row += 1
        elif direction == "left":
            self.current_location.col -= 1
        elif direction == "right":
            self.current_location.col += 1
        print(f"Moved {direction}. Current location: {self.current_location}")

    def shoot_arrow(self):
        if self.wumpus_dead:
            print("Wumpus is already dead.")
        else:
            print(f"Shot arrow towards orientation {self.orientation}.")
            self.wumpus_dead = True  # Assuming a hit for simplicity

# Grid: 4x4 list of lists containing Points
grid = [[Point(row, col) for col in range(4)] for row in range(4)]

# Stack to track next squares to explore
next_squares = []

# List to track unconfirmed signals
unconfirmed_squares = []

# Instantiate the robot at the bottom-left corner (3, 0 in 0-indexed grid)
robot = Robot(start_row=3, start_col=0)


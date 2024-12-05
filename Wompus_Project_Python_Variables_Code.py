class SignalType(Enum):
    GLIMMER = "Glimmer"
    BREEZE = "Breeze"
    STENCH = "Stench"
    GOLD = "Gold"
    NONE = "None"

#This is the Point class to represent a square in the grid
class Point:
    def __init__(self, row: int, col: int, safe: bool = False, confirmed: bool = False, gold: bool = False):
        self.row = row
        self.col = col
        self.safe = safe
        self.confirmed = confirmed
        self.gold = gold

    def __repr__(self):
        return f"Point(row={self.row}, col={self.col}, safe={self.safe}, confirmed={self.confirmed}, gold={self.gold})"

#This is the signal class to represent the signal received from a square
class Signal:
    def __init__(self, point: Point, signal_type: SignalType):
        self.point = point
        self.signal_type = signal_type

    def __repr__(self):
        return f"Signal(point={self.point}, signal_type={self.signal_type.name})"

#Robot class to manage the robot's state and actions
class Robot:
    def __init__(self, start_row: int, start_col: int):
        self.current_location = Point(start_row, start_col)
        self.orientation = 0  #0 means up, 1 means right, 2 means down, 3 means left
        self.has_gold = False
        self.wumpus_dead = False
        self.wumpus_location = None  #Will be a Point when discovered

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

#The following is the grid which is a 4x4 list of lists containing Points
grid = [[Point(row, col) for col in range(4)] for row in range(4)]

#This is the stack to track next squares to explore!!
next_squares = []

#This is the list to track any "unconfirmed" square signals
unconfirmed_squares = []

#This would instantiate the robot at the bottom-left corner (Im not sure how to make it so that it is 0,0 like we established, we could do a similar thing like 3,0 like what I originally proposed but feel free to change it!:))
robot = Robot(start_row=, start_col=)


from nanonav import BLE, NanoBot
import time

### test motors and encoders ###

# Create a NanoBot object
robot = NanoBot()
current_location = Point(start_row, start_col)
orientation = 0  #0 means up, 1 means right, 2 means down, 3 means left
has_gold = False
wumpus_dead = False
wumpus_location = None  #Will be a Point when discovered

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

def moveTo():
    var = 0

def killWumpus():
    var = 0

def computePermutations():
    var = 0

def logSignal():


     time.sleep(5)

     #read from BLE and convert to int
     response = int(ble.read(),2)

     #check for signals
     breeze = 1 & response != 0
     stench = 2 & response != 0
     glimmer = 4 & response != 0
     gold = 8 & response != 0

     signals = [breeze, stench, glimmer, gold]
     signal_types = [SignalType.BREEZE, SignalType.STENCH, SignalType.GLIMMER, SignalType.GOLD]

     #check if there are any signals
     if any(signals):
         #create signal object based on received signals
         for i in range(4):
             if signals[i]:
                 point = grid[robot.current_location.row][robot.current_location.col]
                 signal = Signal(point,signal_types[i])
                 unconfirmed_squares.append(signal)
     else:
         row, col = robot.current_location.row, robot.current_location.col
         directions = [(-1,0), (1,0), (0,-1), (0,1)]
         for i in range(len(directions)):
             r = row + directions[i][0]
             c = col + directions[i][1]
             if 0 <= r < 4 and 0 <= c < 4:
                 grid[r][c].safe = True
                 grid[r][c].confirmed = True
                 next_squares.append(grid[r][c])


#The following is the grid which is a 4x4 list of lists containing Points
grid = [[Point(row, col) for col in range(4)] for row in range(4)]

#This is the stack to track next squares to explore!!
next_squares = []

#This is the list to track any "unconfirmed" square signals
unconfirmed_squares = []

#This would instantiate the robot at the bottom-left corner (Im not sure how to make it so that it is 0,0 like we established, we could do a similar thing like 3,0 like what I originally proposed but feel free to change it!:))
robot = Robot(start_row=, start_col=)

while(current_location != Point(0,0) and has_gold){
    if(len(next_squares) == 0){
        if(wumpus_location != None and !wumpus_dead){
            killWumpus()
        } else{
            success = computePermutations()
            if(!success){
                moveTo(Point(0,0))
            }
        }
    }
    else{
        moveTo(next_squares.pop())
        logSignal()
    }
}





# Move forward for 2 seconds
print(f'encoder 1 start: {robot.get_enc1()}')
robot.m1_forward(30)
robot.m2_forward(30)
time.sleep(2)
print(f'encoder 1 end: {robot.get_enc1()}')

# Stop
robot.stop()
time.sleep(2)

# Move backward for 2 seconds
print(f'encoder 2 start: {robot.get_enc2()}')
robot.m1_backward(30)
robot.m2_backward(30)
time.sleep(2)
print(f'encoder 2 end: {robot.get_enc2()}')

# Stop
robot.stop()

### test Bluetooth ###

# Create a Bluetooth object
ble = BLE(name="Test Name")

ble.send(43)
response = ble.read()
# wait until something changes, indicating a response
while response == 43:
    response = ble.read()
    time.sleep(0.5)

print("Received: ", response)

### test ir sensors ###
while True:
    print(f'left: {robot.ir_left()}    right: {robot.ir_right()}')
    time.sleep(0.5)


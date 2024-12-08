from collections import deque
from sre_parse import State

class Point:
    def __init__(self, row: int, col: int, safe: bool = False, confirmed: bool = False, gold: bool = False):
        self.row = row
        self.col = col
        self.safe = safe
        self.confirmed = confirmed
        self.gold = gold

    def __repr__(self):
        return f"Point(row={self.row}, col={self.col}, safe={self.safe}, confirmed={self.confirmed}, gold={self.gold})"

class Signal:
    def __init__(self, point: Point, signal_type):
        self.point = point
        self.signal_type = signal_type

    def __repr__(self):
        return f"Signal(point={self.point}, signal_type={self.signal_type})"

class Agent:
    def __init__(self,sizex, sizey):
        ##sizex and sizey will give your agent the size of the map
        self.sizex=sizex
        self.sizey=sizey 
        ##TODO: Put the variables you need for your agents here.
        self.grid = [[Point(row, col) for col in range(4)] for row in range(4)]
        self.next_squares = []
        self.unconfirmed_squares = []
        self.x = 0 
        self.y = 0
    ##TODO: define the functions you need here
    def logSignal(self,state):
             safe = True
             for i in range(len(state[0])):
                 if state[0][i] == "BREEZE" or state[0][i] == "STENCH":
                     safe = False
                     break
               #check if there are any signals
             if not safe:
                  #create signal object based on received signals
                  for i in range(len(state[0])):
                      if state[0][i] == "BREEZE" or state[0][i] == "STENCH":
                          point = self.grid[self.x][self.y]
                          signal = Signal(point,state[0][i])
                          self.unconfirmed_squares.append(signal)
                          
             else:
                  row, col = self.y, self.x
                  directions = [(-1,0), (1,0), (0,-1), (0,1)]
                  for i in range(len(directions)):
                      r = row + directions[i][0]
                      c = col + directions[i][1]
                      if 0 <= r < self.sizey and 0 <= c < self.sizex:
                          self.grid[r][c].safe = True
                          self.grid[r][c].confirmed = True
                          self.next_squares.append(self.grid[r][c])
    
    '''
    move(state) will read in the message from the game and return the move the agent will make based on the current information. 
    This is the only function that will be called by the game and the name, param and return must not be changed.
    @param state will be a tuple (messages, 0)      0 is useless here.
           If you use a board which a list(list(set)) where the set keeps all the information about a node on the map, 
           board[i][j]'s up and down, left and right will be like:
                                                   i=2  *   *   *
                                                   i=1  *   *   *
                                                   i=0  *   *   *
                                                       j=0 j=1 j=2
           And the robot will always start at point (0,0).
           The state[0]: messages will be a list of strings which might include: "CONTINUE", "BREEZE", "STENCH", "GLITTER", "KILLED-WUMPUS","GOLD" .
           ["CONTINUE","STENCH"]
           ["FAIL"]
    @return This function should return a string "move_up", "move_down" , "move_left", "move_right" , "shoot_up", "shoot_down", "shoot_right", "shoot_left" based on the current state.
    '''
    def move(self,state):
        ##TODO: Implement your algorithm here
        self.logSignal(state)
        
        return "move_up"
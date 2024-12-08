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
        self.unconfirmed_signals = []
        self.x = 0
        self.y = 0
        self.current_location = Point(0, 0)
        self.current_path = []
        self.current_destination = None
        self.has_gold = False
        self.wumpus_dead = False
        self.wumpus_location = None

    #helper for BFS
    def validMove(self, point, visited):
        if visited[point.row][point.col]:
            return False
        if not point.confirmed or not point.safe:
            return False
        return True

    def moveTo(self, point):
        if self.current_location == point:
            return ""
        if len(self.current_path) == 0:
            #BFS SEARCH TODO: FINISH THIS
            visited = [[False for col in range(4)] for row in range(4)]

            bfs_current = None
            next_locations = [self.current_location]
            while len(next_locations) != 0:
                bfs_current = next_locations.pop()
                visited[bfs_current.row][bfs_current.col] = True

                if(bfs_current == point):
                    self.current_destination = None
                    break

                if self.validMove(Point(bfs_current.row + 1, bfs_current.col), visited):
                    next_locations.insert(0, Point(bfs_current.row + 1, bfs_current.col))
                if self.validMove(Point(bfs_current.row - 1, bfs_current.col), visited):
                    next_locations.insert(0, Point(bfs_current.row - 1, bfs_current.col))
                if self.validMove(Point(bfs_current.row, bfs_current.col + 1), visited):
                    next_locations.insert(0, Point(bfs_current.row, bfs_current.col + 1))
                if self.validMove(Point(bfs_current.row, bfs_current.col - 1), visited):
                    next_locations.insert(0, Point(bfs_current.row, bfs_current.col - 1))

                self.current_path.append(bfs_current)

        step = self.current_path.pop()
        if self.current_location.col + 1  == step.col:
            return "move_right"
        if self.current_location.col - 1 == step.col:
            return "move_left"
        if self.current_location.row - 1 == step.row:
            return "move_up"
        if self.current_location.row + 1 == step.row:
            return "move_down"

    def killWumpus():
        var = 0
    def computePermutations():
        var = 0

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
        #self.logSignal(state)
        move = ""
        if(self.current_location != Point(0,0) and self.has_gold):
          if(len(self.next_squares) == 0):
              if self.wumpus_location != None and not self.wumpus_dead:
                  self.killWumpus()
              else:
                  success = self.computePermutations()
                  if not success:
                      self.moveTo(Point(0,0))
          else:
            if self.current_destination == None:
                self.current_destination = self.next_squares.pop()

        move = self.moveTo(self.current_destination)

        return move

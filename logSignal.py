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
            
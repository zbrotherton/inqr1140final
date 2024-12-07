# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:58:26 2024

@author: angel
"""


#so we would need to keep track of time, depending on how long it takes for the other sensor to detect the line, if the left one detects the white line at time x and the right sensor detects the sensor at time y, we subtract y-x =  to not get a negativz
# make left motor stop until the z time has elpsed
#takes in the two times which the sensors passed the white line, moved the opposite wheel by the amount of time
def adjust(robot, t, t2):
    if t < t2: #if the left sensor detects the white line before the right sensor, t will be left and t2 will be right
        robot.m2_backward(45) #left motor forward with 45 speed
        print("dif: " + str(((t2-t)/1000000000))) #Print the difference in time between the right and left sensor detections in seconds (divide by 1 billion to convert nanoseconds to seconds)
        time.sleep(((t2-t)/1000000000)) #then this will pause the program so the difference in time allows for adjustment
        print("adjustiiiiiiiing")
        robot.stop()
    elif t > t2:
        robot.m1_backward(45)
        print("dif: " + str(((t-t2)/1000000000)))
        time.sleep(((t-t2)/1000000000))
        print("adjusting left")
    robot.stop()
     #this will be necessary since we need to stop both motors after adjusment and then go forward a bit but i need help

def moveForward(robot):
     #start moving forward
    robot.m1_backward(25)
    robot.m2_backward(25)
    t = 0.0
    t2 = 0.0
    left = False
    right = False
    #goes until both sensors have been activated
    while not (left and right):

        #If the left sensor detects the line and hasn't been triggered yet
        if robot.ir_left() and not left:
            t = time.time_ns() #Stores the current time in nanoseconds for the left sensor
            left = True #This marks the left sensor as triggered
            print("right: " + str(right) + " left: " + str(left))
            # And we can print the states of both sensors..

        if robot.ir_right() and not right:
            t2 = time.time_ns()
            right = True
            print("right: " + str(right) + " left: " + str(left))
    print("t: " + str(t) + " t2: " + str(t2))
    print("both sensors are activated")

    adjust(robot, t, t2)

    #fixes orientation

moveForward(robot)

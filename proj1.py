#Written by Christopher Brooks, Jackson Matthews, and Zachary Lynch
#Copyright 2019

import control_interface
import time

def shape(sides):
	if N < 3:	#Polygons need at least 3 sides
		return
		
	perimeter = 2000	#millimeters
	sideLength = perimeter/sides
	buttonPressed = False
	
	velocity = 200	#millimeters per second
	length = 235	#distance between Roomba wheels
	theta = ((sides-2)*180)/sides	#interior angle
	timeSide = (perimeter/velocity)/sides	#10 seconds to travel 2 meters
	print(timeSide)
	angleVelocity = (2*velocity)/length
	timeTurn = 	theta/angleVelocity
	
	while buttonPressed == False:		#waiting for the clean button to be pressed
		time.sleep(0.0125)
		buttonPressed = robot.readButton()
		
	isPressed = False
	i = 0
	while isPressed == False and i < sides:		#driving
		robot.drive(velocity, 0)	#go straight
		
		startTime = time.clock()
		isPressed = False
		while (startTime-time.clock()) < timeSide:		#look for button presses while driving
			buttonPressed = robot.readButton()
			if isPressed == False:
				isPressed = buttonPressed
		
		robot.drive(0,0)	#stop
		time.sleep(0.0125)		#buffer
		robot.drive(0,1)	#turn in place ccwise
		
		startTime = time.clock()
		isPressed = False
		while (startTime-time.clock()) < timeTurn:		#look for button presses while turning
			buttonPressed = robot.readButton()
			if isPressed == False:
				isPressed = buttonPressed
		
		
		robot.drive(0,0)	#stop
		time.sleep(0.0125)		#buffer
		buttonPressed = robot.readButton()
		i = i+1
	
robot = control_interface.ControlInterface()
time.sleep(0.0125)
robot.setState('start')
time.sleep(0.0125)
robot.setState('safe')
N = 4#command line input
shape(N)
robot.setState('passive')
#Written by Christopher Brooks, Jackson Matthews, and Zachary Lynch
#Copyright 2019

import control_interface
import time
import math
import argparse

#The shape function, when given an integer n, gives the roomba directions to drive in an n-sided regular polygon, with a perimeter of 2 meters.

def shape(sides):
	if sides < 3:	#Polygons need at least 3 sides
		print('Invalid Input: Polygons need 3 or more sides.')
		return
		
	perimeter = 2000.0	#millimeters
	sideLength = perimeter/sides
	buttonPressed = False
	velocity = 170.0	#millimeters per second
	length = 235.0	#distance between Roomba wheels in millimeters
	
	theta = (2*math.pi)/sides	#exterior angle in rads
	#theta = (thetaDeg/180)*math.pi		#exterior angle in rads
	timeSide = sideLength/velocity		#delta-t to traverse one side
	angleVelocity = (2*velocity)/length	#copied formula from lecture slides
	timeTurn = theta/angleVelocity		#delta-t to turn to the next side of the polygon
	
	while buttonPressed == False:		#waiting for the clean button to be pressed
		time.sleep(0.0125)
		buttonPressed = robot.readButton()
		
	isPressed = False

	i = 0
	print('Start')
	time.sleep(0.25)	#buffer to prevent unwanted button presses
	
	while i < sides:		#start driving
		robot.drive(velocity, velocity)	#go straight
		
		startTime = time.time()
		isPressed = False
		while (time.time()-startTime) < timeSide:		#look for button presses while driving
			buttonPressed = robot.readButton()
			if isPressed == False and buttonPressed == True:
				isPressed = buttonPressed
				print('Button has been pressed')
		
		if isPressed == True:
			print('Break')
			break			#stop the function
		
		endTime = time.time()
		print(endTime-startTime)
		
		robot.drive(0,0)	#stop
		time.sleep(0.0125)		#buffer
		robot.drive(velocity,-velocity)	#turn in place ccwise
		
		startTime = time.time()
		isPressed = False
		while (time.time()-startTime) < timeTurn:		#look for button presses while turning
			buttonPressed = robot.readButton()
			if isPressed == False and buttonPressed == True:
				isPressed = buttonPressed
				print('Button has been pressed')
		
		if isPressed == True:
			print('Break')
			break			#stop the function
		
		endTime = time.time()
		print(endTime-startTime)
		
		robot.drive(0,0)	#stop
		time.sleep(0.0125)		#buffer
		buttonPressed = robot.readButton()
		i = i+1		#move to the next side
	
	robot.drive(0,0)	#stop moving
	print('Done')
	
	
robot = control_interface.ControlInterface()
time.sleep(0.0125)
robot.setState('passive')
time.sleep(0.0125)
robot.setState('start')
time.sleep(0.0125)
robot.setState('safe')

parser = argparse.ArgumentParser()		#read command line argument
parser.add_argument('val', type=int, help='number of sides')
N = parser.parse_args()		#get number of sides

shape(N.val)

robot.setState('passive')
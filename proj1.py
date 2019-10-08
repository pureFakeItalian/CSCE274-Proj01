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
	velocity = 200.0	#millimeters per second
	length = 235.0	#distance between Roomba wheels in millimeters
	
	theta = (2*math.pi)/sides	#interior angle in rads
	timeSide = sideLength/velocity	#delta-t to traverse one side
	angleVelocity = (2*velocity)/length
	timeTurn = 	theta/angleVelocity		#delta-t to turn to the next side of the polygon
	
	print(sideLength)
	print(theta)
	print(timeSide)				#=== Debugging ===#
	print(angleVelocity)
	print(timeTurn)
	
	timeCalibration = 0.1		#adjustments to time variables; account for nonidealities
	turnCalibration = 0.1
	timeSide = timeSide*timeCalibration
	timeTurn = timeTurn*turnCalibration
	
	while buttonPressed == False:		#waiting for the clean button to be pressed
		time.sleep(0.0125)
		buttonPressed = robot.readButton()
		
	isPressed = False
	i = 0
	print('start')
	time.sleep(0.25)	#buffer
	
	while i < sides:		#driving
		robot.drive(velocity, 0)	#go straight
		
		startTime = time.clock()
		isPressed = False
		
		while (time.clock()-startTime) < timeSide:		#look for button presses while driving
			buttonPressed = robot.readButton()
			print(time.clock()-startTime)
			print(timeSide)
			if isPressed == False and buttonPressed == True:
				isPressed = buttonPressed
				print('button has been pressed')
		
		if isPressed == True:
			print('break')
			break			#stop the program
		
		robot.drive(0,0)	#stop
		time.sleep(0.0125)		#buffer
		robot.drive(0,1)	#turn in place ccwise
		
		startTime = time.clock()
		isPressed = False
		
		while (time.clock()-startTime) < timeTurn:		#look for button presses while turning
			buttonPressed = robot.readButton()
			print(time.clock()-startTime)
			print(timeTurn)
			if isPressed == False and buttonPressed == True:
				isPressed = buttonPressed
				print('button has been pressed')
		
		if isPressed == True:
			print('break')
			break			#stop the program
		
		robot.drive(0,0)	#stop
		time.sleep(0.0125)		#buffer
		buttonPressed = robot.readButton()
		i = i+1
	
	robot.drive(0,0)	#stop
	print('done')
	
	
robot = control_interface.ControlInterface()
time.sleep(0.0125)
robot.setState('passive')
time.sleep(0.0125)
robot.setState('start')
time.sleep(0.0125)
robot.setState('safe')

parser = argparse.ArgumentParser()	#use command line input
parser.add_argument('val', type=int, help='number of sides')
N = parser.parse_args()		#get number of sides
shape(N.val)

robot.setState('passive')
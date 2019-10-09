#Written by Christopher Brooks, Jackson Matthews, and Zachary Lynch
#Copyright 2019
#Only permitted for use in projects written by Christopher Brooks, Jackson Matthews and/or Zachary Lynch

import interface
from struct import unpack
from struct import pack
import time

class ControlInterface:

	#Control Interface is an extension of Interface designed to control the Roomba.
	#This builds off of interface.py, but gives some higher level functionality to the code.

	def __init__(self):
		self.interface = interface.Interface()	#Interface to Roomba
		
		self.packetIds = {7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:2, 20:2, 21:1, 22:2, 23:2, 24:1, 25:2, 26:2, 27:2, 28:2, 29:2, 30:2, 31:2, 34:1, 35:1, 36:1, 37:1, 38:1, 39:2, 40:2, 41:2, 42:2, 43:2, 44:2, 45:1, 46:2, 47:2, 48:2, 49:2, 50:2, 51:2, 54:2, 55:2, 56:2, 57:2, 58:1}
			#a dictionary that records how many bytes each packet id returns
			
		self.states = {'start':128, 'reset':7, 'stop':173, 'passive':128, 'safe':131}
			#states is a dictionary that, when given any of these strings, returns the corresponding opcode

	def setState(self, stateString): #changes the mode of the Roomba
		opcode = self.states[stateString] #gets the proper opcode from the states dictionary
		self.interface.write(chr(opcode))

	def getPacket(self, id):	#A helper command to request packets from the Roomba. Returns an array of bytes.
		self.interface.write(chr(142)+chr(id))	#sends the command to the Roomba
		count = self.packetIds[id]
		retPacket = self.interface.readBytes(count)	#a byte packet from the Roomba
		return retPacket
		
	def readButton(self):	#Detects if the clean button is pressed or not.
		byte = self.getPacket(18)
		button = unpack('B', byte)[0]	#reads the button state ===Currently, this is just the clean button. However, this can be easily fixed===
		return bool(button&0x01)
		
	def drive(self, vr, vl):		#uses the DRIVE DIRECT command to command the roomba
		
		data = pack('>hhh', 145, vr, vl)	#compiles the data into a byte string
		self.interface.write(data)	#sends the drive command to the Roomba
		
#======TEST COMMANDS======#
#robot = ControlInterface()
#sleep(0.0125)
#robot.setState('start')
#robot.setState('safe')
#sleep(0.0125)
#robot.drive(100,100)
#sleep(0.0125)
#robot.drive(0,0)
#robot.setState('passive')
#Written by Christopher Brooks, Jackson Matthews, and Zachary Lynch
#Copyright 2019
#Only permitted for use in projects written by Christopher Brooks, Jackson Matthews and/or Zachary Lynch

import interface    #includes time.sleep()
from struct import unpack
from struct import pack
from time import sleep

class ControlInterface:

	#Control Interface uses Interface to interact with and control the Roomba.
	#This builds off of interface.py, but gives some higher level functionality to the code.

	def __init__(self):
		self.interface = interface.Interface()	#Interface to Roomba
		
		self.packetIds = {7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:2, 20:2, 21:1, 22:2, 23:2, 24:1, 25:2, 26:2, 27:2, 28:2, 29:2, 30:2, 31:2, 34:1, 35:1, 36:1, 37:1, 38:1, 39:2, 40:2, 41:2, 42:2, 43:2, 44:2, 45:1, 46:2, 47:2, 48:2, 49:2, 50:2, 51:2, 54:2, 55:2, 56:2, 57:2, 58:1}
			#a dictionary that records how many bytes each packet id returns
			
		self.states = {'start':128, 'reset':7, 'stop':173, 'passive':128, 'safe':131}
			#states is a dictionary that, when given any of these strings, returns the corresponding opcode
			
		self.buttons = [0,0,0,0,0,0,0,0]
			#an array that keeps track of each button state: 0->unpressed, 1->pressed
			#buttons are: clock, schedule, day, hour, minute, dock, spot, clean; respectively

	def setState(self, stateString): #changes the mode of the Roomba
		opcode = self.states[stateString] #gets the proper opcode from the states dictionary
		self.interface.write(chr(opcode))

	def getPacket(id, self):	#A helper command to request packets from the Roomba. Returns an array of bytes.
		self.interface.write(chr(142)+chr(id))	#sends the command to the Roomba
		count = self.packetIds[id]
		retPacket = self.interface.readBytes(count)	#a byte packet from the Roomba
		bytes = unpack('B', retPacket)	#using unpack to create a tuple of bytes
		return bytes
		
	def readButtons(self):	#Gets the sensor data of the buttons and updates the buttons array.
		packet = self.interface.getPacket(18)
		packetBin = bin(packet[0])	#byte -> bit string
		for i in packetBin:
			self.buttons[i] = packetBin[i]

	def drive(self, v, r):
		#dummy1, dummy2, v1, v2 = pack('<i', v&0xF)	#pack returns 4 bytes for each int, but we only want
		#dummy3, dummy4, r1, r2 = pack('<i', r&0xF)	#the last two for each value cause they're so small
		self.interface.write(pack('>B2h', 137, v, r))	#sends the drive command to the Roomba
		
		
self = ControlInterface()
sleep(0.0125)
self.setState('start')
sleep(0.0125)
self.drive(50, 0)
sleep(0.0125)
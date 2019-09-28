#Written by Christopher Brooks, Jackson Matthews, and Zachary Lynch
#Copyright 2019
#Only permitted for use in projects written by Christopher Brooks, Jackson Matthews and/or Zachary Lynch

from serial import Serial
from time import sleep
class Interface:

	#Interface serves as a manager for the serial connection between the Raspberry Pi and the Roomba.
	#Each command in the interface is sending a series of bytes to the Roomba.
	#Each command is defined beforehand and can be called from whereever the interface is imported.

	#Command Definitions
	def __init__(self):
		self.connection = Serial('/dev/ttyUSB0', baudrate=115200)	#serial connection to Roomba

	def powerOff(self):
		self.connection.write(chr(133))

	def readBytes(n, self):	#returns an array of n bytes
		ret = self.connection.read(n)
		return ret

	def write(data, self):
		self.connection.write(data)

	def close(self):
		self.connection.close()

#======TEST COMMANDS FOR VERIFYING A CONNECTION======#
#interface = Interface()
#interface.powerOff()
#interface.close()
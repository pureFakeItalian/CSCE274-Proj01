import serial
import time

class Interface:
    def __init__(self):
        self.connector
    def open(self):
        #self.connection.open()
        kDelay = 0.0125
        time.sleep(kDelay)
    def connect(self):
        connection = serial.Serial('/dev/ttyUSB0', baudrate=115200)
    def start(self):
        connection.write(chr(128))
    def restart(self):
        connection.write(chr(7))
    def stop(self):
        connection.write(chr(173))
    def poweroff(self):
        connection.write(chr(133))
    def read(self):
        connection.read(1)
    def passiveMode(self):
        # Start command changes mode to passive
        # Not sure if there's strictly a passive opcode
        connection.write(chr(128)) 
    def safeMode(self):
        connection.write(chr(131)) 
    def drive(self):
        connection.write(chr(137))
        # [Velocity high byte] [Velocity low byte] [radius high byte] 
        # [radius low byte]
        # P.13 - OI Manual
        #
        # Test drive
        # Should drive in reverse @ -200 mm/s & turn @ radius of 500 mm
        connection.write(chr(255))
        connection.write(chr(56))
        connection.write(chr(1))
        connection.write(chr(244))
        

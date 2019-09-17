import serial
import time

class Interface:
    def __init__(self):
        self.connection = serial.Serial('/dev/ttyUSB0', baudrate=115200)
    def open(self):
        #self.connection.open()
        kDelay = 0.0125
        time.sleep(kDelay)
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
        

import Tkinter as tk
import threading
import serial

class ship:
   heading = 0

class enviorment(ship):
   windSpeed = 0
   windDirection = 0

   def set_windSpeedDIR(self,envData):
       vaneAngle       = 0
       vaneAngle       = envData % 1000
       self.windDirection   = abs(self.heading - vaneAngle)
       self.windSpeed       = (envData-vaneAngle)/1000

   def get_windSpeed(self):
       return self.windSpeed

   def get_windDIR(self):
       return self.windDirection


def btComms():
	data = ""
	if(blSerial.in_waiting > 0):
			data =blSerial.readline()
			data = int(data)
	return data


env = enviorment()

blSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
print("Bluetooth connected")

while 1:
	envData = btComms()
	if type(envData) is int:
		env.set_windSpeedDIR(envData)
		print("Wind Speed:")
		print(env.get_windSpeed())
		print("Wind Direction:")
		print(env.get_windDIR())
		
	
	






















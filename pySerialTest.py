import serial

blSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
print("Bluetooth connected")
try:
	while 1:
		data =blSerial.readline()
		print(data)
except KeyboardInterrupt:
	print("Quit")

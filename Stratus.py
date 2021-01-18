#Senior Design Project: SailingHub
#Contributors: Daniel McGinnis, Garnett Altenberger, Joe Flom, Drew Blackburn
#Date: 10/30/2018

import Tkinter as tk
import serial

LARGE_FONT= ("Verdana", 12)

class App(tk.Tk):
  
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.shared_data = {"shipHeading": tk.StringVar(),
                           "shipSpeed": tk.StringVar(),
                           "windSpeed": tk.StringVar(),
                           "windDir": tk.StringVar(),}
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
      
		self.frames = {}

		for F in (MainHub, Guide):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
      
		self.show_frame(MainHub)
      

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class MainHub(tk.Frame, tk.Tk):
  
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		lbl_heading = tk.Label(self, textvariable=self.controller.shared_data["shipHeading"], font=LARGE_FONT,bd=1)
		lbl_heading.grid(row=0,column=0,pady=10,padx=10)
		lbl_shipSpeed = tk.Label(self, textvariable=self.controller.shared_data["shipSpeed"], font=LARGE_FONT, bd=1)
		lbl_shipSpeed.grid(row=0,column=1,pady=10,padx=10)
		lbl_windSpeed = tk.Label(self, textvariable=self.controller.shared_data["windSpeed"], font=LARGE_FONT,bd=1)
		lbl_windSpeed.grid(row=1,column=0,pady=10,padx=10)
		lbl_windDir = tk.Label(self, textvariable=self.controller.shared_data["windDir"], font=LARGE_FONT, bd=1)
		lbl_windDir.grid(row=1,column=1,pady=10,padx=10)

		button1 = tk.Button(self, text="Sailing Guide",
                   command=lambda: controller.show_frame(Guide))
		button1.grid(row=2,columnspan=2)

class Guide(tk.Frame, tk.StringVar):
  
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label1 = tk.Label(self, textvariable=self.controller.shared_data["shipHeading"], font=LARGE_FONT)
		label1.pack(pady=10,padx=10)
		button1 = tk.Button(self, text="Home",
                   command=lambda: controller.show_frame(MainHub))
		button1.pack()

class vessel:
	shipHeading = 180
	shipSpeed = 5

class enviorment():
	windSpeed = 0
	windDirection = 0

	def set_windSpeedDIR(self,envData):
		vaneAngle       = 0
		vaneAngle       = envData % 1000
		self.windDirection   = abs(ship.shipHeading - vaneAngle)
		self.windSpeed       = (envData-vaneAngle)/1000

	def get_windSpeed(self):
		return self.windSpeed

	def get_windDIR(self):
		return self.windDirection
  
def DoSomething():
	print("I am doing something!")
	app.shared_data["shipHeading"].set("Ship Heading: " + str(ship.shipHeading) + " Degrees")
	app.shared_data["shipSpeed"].set("Ship Speed: " + str(ship.shipSpeed) + " Knots")
	envData = btComms()
	if type(envData) is int:
		env.set_windSpeedDIR(envData)
		app.shared_data["windSpeed"].set("Wind Speed: " + str(env.get_windSpeed()) + " mph")
		app.shared_data["windDir"].set("Ship Direction: " + str(env.get_windDIR()) + " Degrees")
	app.after(1000, DoSomething)

def btComms():
	data = ""
	if(blSerial.in_waiting > 0):
		data =blSerial.readline()
		data = int(data)
	return data

app = App()
blSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
env = enviorment()
ship = vessel()
app.after(1000, DoSomething)
app.mainloop()


























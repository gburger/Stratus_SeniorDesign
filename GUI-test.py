import Tkinter as tk
import threading

class App(threading.Thread):

   def __init__(self):
       threading.Thread.__init__(self)
       self.start()

   def callback(self):
       self.root.quit()

   def run(self):
       self.root = tk.Tk()
       self.root.protocol("WM_DELETE_WINDOW", self.callback)
       self.s = tk.StringVar()
       self.s.set('Hello World')
       label = tk.Label(self.root, textvariable=self.s)
       label.pack()

       self.root.mainloop()

app = App()
print('Now we can continue running code while mainloop runs!')
app.s.set("Daniel")
i = 0
for i in range(100000):
   print(i)

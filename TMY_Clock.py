"""TMY_Clock
Typical Meterological Year analog clock face
"""

try:
	import Tkinter
except:
	import tkinter as Tkinter

import math	# Required For Coordinates Calculation
import time	# Required For Time Handling

class TMY_Clock(Tkinter.Tk):
    """"""
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x = 154    # Center point x
        self.y = 154    # center point y
        self.length = [100,125,125]  # stick length
        self.width = [4,2,1]
        self.creating_all_function_trigger()
        self.color = 254

    # Creating Trigger for other functions
    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.creating_background_()
        self.creating_sticks()
        return

    # creating canvas
    def create_canvas_for_shapes(self):
        self.canvas = Tkinter.Canvas(self, bg='blue', width=312, height=312)
        self.canvas.pack(expand='no',fill='both')
        return

    # creating background
    def creating_background_(self):
        #self.image=Tkinter.PhotoImage(file='clock.gif')
        #self.canvas.create_image(150, 150, image=self.image)
        self.clkface = self.canvas.create_oval(8,8,308,308,fill='gray50', outline='red', width=4)
        return

    # creating moving sticks
    def creating_sticks(self):
        self.sticks=[]
        for n,i in enumerate(self.length):
            store = self.canvas.create_line(self.x,self.y,self.x+i,self.y+n,width=self.width[n],fill='red')
            self.sticks.append(store)
        return

    def update_class(self):
        now = time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime('%I', t))*5
        now=(hour,now.tm_min,now.tm_sec)
        # changing the sticks coordinates in a loop, only moves hands at 0 crossing
        # for n,i in enumerate(now):
        #     x,y=self.canvas.coords(self.sticks[n])[0:2]
        #     cr=[x,y]
        #     cr.append(self.length[n]*math.cos(math.radians(i*6)-math.radians(90))+self.x)
        #     cr.append(self.length[n]*math.sin(math.radians(i * 6) - math.radians(90)) + self.x)
        #     self.canvas.coords(self.sticks[n],tuple(cr))

        # changing the sticks coordinates continuously
        # Hour stick
        x, y = self.canvas.coords(self.sticks[0])[0:2]
        cr = [x,y]
        cr.append(self.length[0] * math.cos(math.radians((now[0] * 6) + (now[1] * 6) / 12) - math.radians(90)) + self.x)
        cr.append(self.length[0] * math.sin(math.radians((now[0] * 6) + (now[1] * 6) / 12) - math.radians(90)) + self.x)
        self.canvas.coords(self.sticks[0], tuple(cr))

        # minute stick
        x, y = self.canvas.coords(self.sticks[1])[0:2]
        cr = [x,y]
        cr.append(self.length[1] * math.cos(math.radians((now[1] * 6) + (now[2] * 6) / 60) - math.radians(90)) + self.x)
        cr.append(self.length[1] * math.sin(math.radians((now[1] * 6) + (now[2] * 6) / 60) - math.radians(90)) + self.x)
        self.canvas.coords(self.sticks[1], tuple(cr))

        # second stick
        x, y = self.canvas.coords(self.sticks[2])[0:2]
        cr = [x, y]
        cr.append(self.length[2] * math.cos(math.radians((now[2] * 6)) - math.radians(90)) + self.x)
        cr.append(self.length[2] * math.sin(math.radians((now[2] * 6)) - math.radians(90)) + self.x)
        self.canvas.coords(self.sticks[2], tuple(cr))

        self.change_color(int((now[2]/60)*255))

        return

    def change_color(self,color):
        #self.color = (self.color+1) % 255
        #color = self.color
        bg = '#'+bytes([color,color,color]).hex()
        self.canvas.itemconfig(self.clkface, fill=bg)
        return





if __name__=='__main__':
    root=TMY_Clock()

    while True:
        root.update()
        root.update_idletasks()
        root.update_class()
        #root.after(1000, root.change_color)

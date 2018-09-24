#!/usr/bim/python3
#matplotlib
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
#tkinter
import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Vedrana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100) #matplotlib
a = f.add_subplot(111)

def animate(i):
	pullData = open("sampleData.txt","r").read()
	dataList = pullData.split (\n)
	xList = []
	yList = []
	for eachLine in dataList:
		if len(eachLine) > 1:
			x, y = eachLine.split(',')
			xList.append(int(x))
			yList.append(int(y))

	a.clear()
	a.plot(xList, yList)
	

class SeaofBTCapp(tk.Tk): #class that is subclass of tkinter
	
	def __init__(self, *args, **kwargs): #this runs first after class is called	
		tk.Tk.__init__(self, *args, **kwargs)#initialize tkinter
		tk.Tk.wm_title(self, "Sea of BTC client")
		
		container = tk.Frame(self)	#main frame	
		container.pack(side="top", fill="both", expand = True)		
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo, PageThree):
			frame = F(container, self)	
			self.frames[F] = frame	
			frame.grid(row=0, column = 0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__ (self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label (self, text="Start Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button = ttk.Button(self, text="Visit Page 1",
							command = lambda: controller.show_frame(PageOne))
		button.pack()
		button2 = ttk.Button(self, text="Visit Page 2",
							command = lambda: controller.show_frame(PageTwo))
		button2.pack()
		button3 = ttk.Button(self, text="Graph Page",
							command = lambda: controller.show_frame(PageThree))
		button3.pack()

class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label (self, text="Page One!!!", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
	
		button1 = ttk.Button(self, text="Back to Home",
							command = lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text="Page Two",
							command = lambda: controller.show_frame(PageTwo))
		button2.pack()
		
class PageTwo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label (self, text="Page Two!!!", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
	
		button1 = ttk.Button(self, text="Back to Home",
							command = lambda: controller.show_frame(StartPage))
		button1.pack()
		
		button2 = ttk.Button(self, text="Page One",
							command = lambda: controller.show_frame(PageOne))
		button2.pack()

class PageThree(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label (self, text="Graph Page!", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
	
		button1 = ttk.Button(self, text="Back to Home",
							command = lambda: controller.show_frame(StartPage))
		button1.pack()

		

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill = tk.BOTH, expand = True)

		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
ani = animaton.FuncAnimation(f, animate, interval = 1000)
app.mainloop()

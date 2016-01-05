#!/usr/bin/env python
import matplotlib
matplotlib.use('tkagg')
import pylab
import Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import L3G4200D

l3d4200d = L3G4200D.L3G4200D()

root = Tkinter.Tk()
root.wm_title("L3G4200D Gyro Sensor")

xAchse=pylab.arange(0,100,1)
yAchse=pylab.array([0]*100)

fig = pylab.figure(1)

ax1 = fig.add_subplot(311)
ax1.grid(True)
ax1.set_xlabel("Time")
ax1.set_ylabel("X Amplitude")
ax1.axis([0,100,-200.,200.])
line1=ax1.plot(xAchse,yAchse,'-')

ax2 = fig.add_subplot(312)
ax2.grid(True)
ax2.set_xlabel("Time")
ax2.set_ylabel("Y Amplitude")
ax2.axis([0,100,-200.,200.])
line2=ax2.plot(xAchse,yAchse,'-')

ax3 = fig.add_subplot(313)
ax3.grid(True)
ax3.set_xlabel("Time")
ax3.set_ylabel("Z Amplitude")
ax3.axis([0,100,-200.,200.])
line3=ax3.plot(xAchse,yAchse,'-')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

values=[0,0,0]
for i in range(3):
    values[i] = [0 for x in range(100)]

def DataGenerator():
  global values,wScale2

  data = l3d4200d.readList()
  for i in range(3):
    values[i].append(data[i])
  root.after(int(wScale2['to'])-wScale2.get(),DataGenerator)

def RealtimePlotter():
  global values,wScale,wScale2
  NumberSamples=min(len(values[0]),wScale.get())
  CurrentXAxis=pylab.arange(len(values[0])-NumberSamples,len(values[0]),1)
  line1[0].set_data(CurrentXAxis,pylab.array(values[0][-NumberSamples:]))
  line2[0].set_data(CurrentXAxis,pylab.array(values[1][-NumberSamples:]))
  line3[0].set_data(CurrentXAxis,pylab.array(values[2][-NumberSamples:]))
  ax1.axis([CurrentXAxis.min(),CurrentXAxis.max(),-200.,200.])
  ax2.axis([CurrentXAxis.min(),CurrentXAxis.max(),-200.,200.])
  ax3.axis([CurrentXAxis.min(),CurrentXAxis.max(),-200.,200.])
  canvas.draw()
  root.after(500,RealtimePlotter)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tkinter.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tkinter.BOTTOM)

wScale = Tkinter.Scale(master=root,label="View Width:", from_=3, to=1000,sliderlength=30,length=ax1.get_frame().get_window_extent().width, orient=Tkinter.HORIZONTAL)
wScale2 = Tkinter.Scale(master=root,label="Generation Speed:", from_=1, to=1000,sliderlength=30,length=ax1.get_frame().get_window_extent().width, orient=Tkinter.HORIZONTAL)
wScale2.pack(side=Tkinter.BOTTOM)
wScale.pack(side=Tkinter.BOTTOM)

wScale.set(990)
wScale2.set(wScale2['to']-10)

root.protocol("WM_DELETE_WINDOW", _quit)
root.after(500,DataGenerator)
root.after(500,RealtimePlotter)
Tkinter.mainloop()

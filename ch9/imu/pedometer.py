import Tkinter as tk
import LSM303DLHC
#import MPU6050

sensor = LSM303DLHC.LSM303DLHC()
#sensor = MPU6050.MPU6050()

root = tk.Tk()
root.wm_title("RPi Pedometer")

pedometer = tk.LabelFrame(root, text="Pedometer", height=220, width=300, font=("Helvetica", 16))

step = 0
stepV = tk.IntVar()
stepV.set(step)
stepLabel = tk.Label(pedometer, textvariable=stepV, font=("Helvetica", 100))
stepLabel.place(x=50, y=0, width=200, height=180)
pedometer.pack(pady=10)

limit = 10
lastvalue = 0.0
lastdir = 0
lastextremes = [0.0, 0.0]
lastdiff = 0.0
lastmatch = -1

def calc_stepstep(ax, ay, az):
  h = 480
  yoffset = h * 0.5
  scale = h * 0.5 / 60
  global step, lastvalue, lastdir, lastextremes, lastdiff, lastmatch
  v = yoffset + (ax + ay + az) * scale / 3
  direction = 0 if v > lastvalue else 1
  if direction == 1 - lastdir:
    lastextremes[direction] = lastvalue
    diff = abs(lastextremes[direction] - lastextremes[1-direction])
    if diff > limit:
      # if diff is as large as previous and previous is large enough
      if (diff > lastdiff*2/3) and (lastdiff > diff/3) and (lastmatch != 1 - direction):
        step = step + 1
        lastmatch = direction
      else:
        lastmatch = -1
    lastdiff = diff
  lastdir = direction
  lastvalue = v

def update():
  global data, step
  data = sensor.read()
  calc_stepstep(float(data[0])/100, float(data[1])/100, float(data[2])/100)
  #calc_stepstep(float(data[0]*10), float(data[1]*10), float(data[2]*10))
  root.after(50, update)
  stepV.set(step)

def clear_value():
  global step
  step = 0

clearButton = tk.Button(root, text="Clear", command=clear_value, font=("Helvetica", 50))
clearButton.pack(pady=20, side="bottom")

update()
root.mainloop()

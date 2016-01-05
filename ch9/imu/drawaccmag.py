import Tkinter as tk
import LSM303DLHC

lsm = LSM303DLHC.LSM303DLHC()

root = tk.Tk()
root.wm_title("LSM303DLHC Accel/Mag Sensor")

accelerometer = tk.LabelFrame(root, text="Accelerometer", height=150, width=300, font=("Helvetica", 16))

ax = tk.Label(accelerometer, text="X:", font=("Helvetica", 16))
ax.place(x=50, y=0, width=50, height=40)

ay = tk.Label(accelerometer, text="Y:", font=("Helvetica", 16))
ay.place(x=50, y=30, width=50, height=40)

az = tk.Label(accelerometer, text="Z:", font=("Helvetica", 16))
az.place(x=50, y=60, width=50, height=40)

accV = []
for i in range(3):
    var = tk.StringVar()
    accV.append(var)
    accV[i].set(str(0.0))
    aval = tk.Label(accelerometer, textvariable=accV[i], font=("Helvetica", 16))
    aval.place(x=100, y=0+30*i, width=90, height=40)

magnetometer = tk.LabelFrame(root, text="Magnetometer", height=150, width=300, font=("Helvetica", 16))

mx = tk.Label(magnetometer, text="X:", font=("Helvetica", 16))
mx.place(x=50, y=0, width=50, height=40)

my = tk.Label(magnetometer, text="Y:", font=("Helvetica", 16))
my.place(x=50, y=30, width=50, height=40)

mz = tk.Label(magnetometer, text="Z:", font=("Helvetica", 16))
mz.place(x=50, y=60, width=50, height=40)

magV = []
for i in range(3):
    var = tk.StringVar()
    magV.append(var)
    magV[i].set(str(0.0))
    mval = tk.Label(magnetometer, textvariable=magV[i], font=("Helvetica", 16))
    mval.place(x=100, y=0+30*i, width=90, height=40)

accelerometer.pack(pady=10)
magnetometer.pack(pady=10)

def update():
  data = lsm.read()
  root.after(200, update)

  try:
    for i, var in enumerate(accV):
        var.set("{0:2.2f}".format(float(data[i])/100.0))

    for i, var in enumerate(magV):
        var.set("{0:2.2f}".format(float(data[i+3])/100.0))

  except ValueError:
    print "string to float error"

update()
root.mainloop()

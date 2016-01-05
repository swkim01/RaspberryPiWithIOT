import Tkinter as tk
import math
import LSM303DLHC
#import MPU6050
#import HMC5883L

sensor = LSM303DLHC.LSM303DLHC()
#mpu = MPU6050.MPU6050()
#sensor = HMC5883L.HMC5883L()

root = tk.Tk()
root.wm_title("Electronic Compass")

angleV = tk.StringVar()
angleV.set("0")
value = tk.Label(root, textvariable=angleV, font=("Helvetica", 14))
value.place(x=150, y=0, width=90, height=40)
value.pack(side="top", pady=10)

# COMPASS
canvas = tk.Canvas(root, bg="white", height=300, width=300)
canvas.pack(side="bottom")

#canvas.place(x=300, y=0, width=300, height=300)
canvas.create_oval(20, 20, 280, 280, outline="black", width=2)
canvas.create_oval(50, 50, 250, 250, outline="black", width=2)
#canvas.create_line(150, 250, 150, 50, fill="blue")
#canvas.create_line(50, 150, 250, 150, fill="blue")
for i in range(36):
    theta = 10 * i * math.pi / 180
    s = math.sin(theta)
    c = math.cos(theta)
    if i % 3 == 0:
        canvas.create_line(150 + 100 * s, 150 + 100 * c, 150 + 120 * s, 150 + 120 * c)
    else:
        canvas.create_line(150 + 100 * s, 150 + 100 * c, 150 + 110 * s, 150 + 110 * c)

xN = tk.Label(canvas, text="N", bg="white", font=("Helvetica", 14))
xE = tk.Label(canvas, text="E", bg="white", font=("Helvetica", 14))
xS = tk.Label(canvas, text="S", bg="white", font=("Helvetica", 14))
xW = tk.Label(canvas, text="W", bg="white", font=("Helvetica", 14))

#xN.place(x=143, y=30)
xN.place(x=143, y=60)
#xE.place(x=260, y=142)
xE.place(x=230, y=142)
#xS.place(x=144, y=260)
xS.place(x=144, y=220)
#xW.place(x=30, y=142)
xW.place(x=60, y=142)

center = 150, 150
triangle1 = [(center[0],center[1]-100), (center[0]-10,center[1]), (center[0]+10,center[1])]
polygon_item1 = canvas.create_polygon(triangle1, fill="red")
triangle2 = [(center[0],center[1]+100), (center[0]+10,center[1]), (center[0]-10,center[1])]
polygon_item2 = canvas.create_polygon(triangle2, fill="blue")

def update():

  angle_deg = sensor.calcTiltHeading()
  #sensor.read()
  #data = mpu.read()
  #angle_deg = sensor.calcTiltHeading(data[0], data[1], data[2])

  root.after(200, update)

  #compass point
  angleV.set("{0:3.2f}".format(angle_deg))

  cangle = math.cos(angle_deg*math.pi/180.)
  sangle = math.sin(angle_deg*math.pi/180.)

  newxy = []
  for x,y in triangle1:
    nx = cangle * (x - center[0]) + sangle * (y - center[1]) + center[0]
    ny = -sangle * (x - center[0]) + cangle * (y - center[1]) + center[1]
    newxy.append(nx)
    newxy.append(ny)
    canvas.coords(polygon_item1, *newxy)
  newxy = []
  for x,y in triangle2:
    nx = cangle * (x - center[0]) + sangle * (y - center[1]) + center[0]
    ny = -sangle * (x - center[0]) + cangle * (y - center[1]) + center[1]
    newxy.append(nx)
    newxy.append(ny)
    canvas.coords(polygon_item2, *newxy)

update()
root.mainloop()

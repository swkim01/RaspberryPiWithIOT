from Tkinter import *

root = Tk()
root.title("Callback and Event Test")
root.geometry("100x100+300+300")

def callback():
    print "button clicked"

button = Button(root, text="Click me!", width=10, command=callback)
button.pack(padx=10, pady=10)
root.mainloop()

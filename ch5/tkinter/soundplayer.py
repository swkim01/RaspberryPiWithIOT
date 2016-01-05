import pygame.mixer
from Tkinter import *
import tkFileDialog

class MusicPlayer(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        button_opt = {'side': LEFT, 'padx': 5, 'pady': 5 }
        Button(self, text="Load", command=self.askopenfile).pack(**button_opt)
        Button(self, text="Play", command=self.playfile).pack(**button_opt)
        Button(self, text="Stop", command=self.stopfile).pack(**button_opt)
        self.volume=DoubleVar()
        self.volume.set(1.0)
        Scale(self, variable=self.volume, from_=0.0, to=1.0,
                    resolution=0.1, command=self.changevolume,
                    orient=HORIZONTAL).pack(**button_opt)

    def askopenfile(self):
        self.filename = tkFileDialog.askopenfilename(initialdir="/home/pi")
        if self.filename.endswith('.mp3'):
            pygame.mixer.music.load(self.filename)
        else:
            self.track = pygame.mixer.Sound(self.filename)

    def playfile(self):
        if self.filename.endswith('.mp3'):
            pygame.mixer.music.play()
        elif self.track != None:
            self.track.play(loops=-1)

    def stopfile(self):
        if self.filename.endswith('.mp3'):
            pygame.mixer.music.stop()
        elif self.track != None:
            self.track.stop()

    def changevolume(self, v):
        if self.filename.endswith('.mp3'):
            pygame.mixer.music.set_volume(self.volume.get())
        elif self.track != None:
            self.track.set_volume(self.volume.get())

def shutdown():
    pygame.mixer.stop()
    tk.destroy()

if __name__ == "__main__" :
    pygame.mixer.init(48000, -16, 1, 1024)
    tk = Tk()
    tk.title("Music Player")
    tk.geometry("300x100+300+300")
    panel = MusicPlayer(tk)
    panel.pack()
    tk.protocol("WM_DELETE_WINDOW", shutdown)
    tk.mainloop()

import pygame.mixer
from time import sleep

pygame.mixer.init(48000, -16, 1, 1024)
#pygame.mixer.init()
#sound = pygame.mixer.Sound("/home/pi/Downloads/music.wav")
pygame.mixer.music.load("/home/pi/Downloads/music.wav")
pygame.mixer.music.play()
sleep(5.0)

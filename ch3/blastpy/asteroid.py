import pygame
import math, random

scale=[1.25, 0.9, 0.4]

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, type, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface([45, 40])
        self.surface.fill(pygame.Color(0, 0, 0))
        self.color = pygame.Color(255, 255, 255)
        pygame.draw.line(self.surface, self.color, (5, 40), (0, 25), 2)
        pygame.draw.line(self.surface, self.color, (0, 25), (0, 10), 2)
        pygame.draw.line(self.surface, self.color, (0, 10), (20, 10), 2)
        pygame.draw.line(self.surface, self.color, (20, 10), (15, 0), 2)
        pygame.draw.line(self.surface, self.color, (15, 0), (30, 0), 2)
        pygame.draw.line(self.surface, self.color, (30, 0), (45, 10), 2)
        pygame.draw.line(self.surface, self.color, (45, 10), (25, 20), 2)
        pygame.draw.line(self.surface, self.color, (25, 20), (45, 30), 2)
        pygame.draw.line(self.surface, self.color, (45, 30), (35, 40), 2)
        pygame.draw.line(self.surface, self.color, (35, 40), (25, 35), 2)
        pygame.draw.line(self.surface, self.color, (25, 35), (5, 39), 2)
        self.w, self.h = w, h
        self.x, self.y = 30, 30 + random.randint(0, 440)
        self.heading = 0
        self.speed = 0.5 + random.random() * 1.5
        self.rot_velocity = 0.01
        self.heading = random.random() * 10.0
        self.twist = random.random() * 10.0
        self.type = type
        self.scale = scale[type]
        self.surface = pygame.transform.rotozoom(self.surface, 0, self.scale)
        self.image = self.surface
        self.rect = self.image.get_rect()

    def update(self):
        self.image = pygame.transform.rotate(self.surface, self.twist)
        self.x = self.x + (math.sin(self.heading) * self.speed)
        self.y = self.y - (math.cos(self.heading) * self.speed)
        self.twist = self.twist + self.rot_velocity

        if (self.x < 0):
           self.x += self.w
        if (self.x > self.w):
           self.x -= self.w
        if (self.y < 0):
           self.y += self.h
        if (self.y > self.h):
           self.y -= self.h

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.heading = self.twist

import pygame
import math

class SpaceShip(pygame.sprite.Sprite):

    def __init__(self, w, h, heading, speed):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface([20, 22])
        self.surface.fill(pygame.Color(0, 0, 0))
        self.color = pygame.Color(0, 255, 255)
        pygame.draw.line(self.surface, self.color, (2, 21), (10, 0), 3)
        pygame.draw.line(self.surface, self.color, (10, 0), (18, 20), 3)
        pygame.draw.line(self.surface, self.color, (4, 15), (9, 15), 3)
        pygame.draw.line(self.surface, self.color, (16, 15), (11, 15), 3)
        self.w, self.h = w, h
        self.x, self.y = w/2, h/2
        self.heading = heading
        self.speed = speed
        self.lives = 3

    def update(self):
        if self.lives <= 0:
            return
        self.image = pygame.transform.rotate(self.surface, - self.heading * 180 / 3.14)
        self.x = self.x + (math.sin(self.heading) * self.speed)
        self.y = self.y - (math.cos(self.heading) * self.speed)

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

    def accelerate(self):
        self.speed += 0.08
        if (self.speed > 3.0):
            self.speed = 3

    def decelerate(self):
        self.speed -= 0.08
        if (self.speed < 0.3):
            self.speed = 0.3

    def turn_right(self):
        self.heading += 0.05

    def turn_left(self):
        self.heading -= 0.05

    def damage(self):
        if (self.lives > 0):
            self.lives -= 1
            self.x, self.y = self.w/2, self.h/2
            self.heading = 0
            self.speed = 0

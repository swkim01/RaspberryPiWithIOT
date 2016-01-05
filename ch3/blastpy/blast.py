import pygame
import math

class Blast(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface([3, 3])
        self.surface.fill(pygame.Color(0, 0, 0))
        self.color = pygame.Color(0, 255, 255)
        pygame.draw.circle(self.surface, self.color,
                         (1, 1), 2, 2)
        self.x, self.y = 0, 0
        self.heading = 0
        self.speed = 5
        self.live = 0
        self.image = self.surface
        self.rect = self.surface.get_rect()

    def update(self):
        self.x = self.x + (math.sin(self.heading) * self.speed)
        self.y = self.y - (math.cos(self.heading) * self.speed)
        self.rect.center = (self.x, self.y)

    def firedfrom(self, s):
        self.heading = s.heading
        self.x = s.x
        self.y = s.y
        self.update()

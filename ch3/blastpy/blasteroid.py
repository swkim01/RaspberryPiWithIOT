import pygame, sys
import math
from spaceship import *
from asteroid import *
from blast import *

ASTEROID_SCORES = [20, 50, 100]
WIDTH, HEIGHT = 500, 500
TOTAL_SCORE = 0

def main():
    global SHIP, WINDOW, FPS, ASTEROID_LIST, BLAST_LIST

    pygame.init()
    FPS = pygame.time.Clock()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    SHIP = SpaceShip(WIDTH, HEIGHT, 0, 0)
    ASTEROID_LIST = pygame.sprite.Group()
    for i in range(4):
        asteroid = Asteroid(0, WIDTH, HEIGHT)
        ASTEROID_LIST.add(asteroid)
    BLAST_LIST = pygame.sprite.Group()
    
    pygame.key.set_repeat()
    
    while True:
        #get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    terminate()
    
            keystate = pygame.key.get_pressed()
            if (keystate[pygame.K_SPACE] and SHIP.lives > 0):
                blast = Blast()
                blast.firedfrom(SHIP)
                BLAST_LIST.add(blast)
    
        keystate = pygame.key.get_pressed()
        heading = keystate[pygame.K_UP] - keystate[pygame.K_DOWN]
        direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        if (heading > 0):
            SHIP.accelerate()
        elif (heading < 0):
            SHIP.decelerate()
        if (direction > 0):
            SHIP.turn_right()
        elif (direction < 0):
            SHIP.turn_left()

        moveObjects()
        processCollisions()
        WINDOW.fill(pygame.Color(0, 0, 0))
        drawObjects()
        displayScore()
        displayShipLivesGameOver()
    
def terminate():
    pygame.quit()
    sys.exit()

def moveObjects():
    SHIP.update()
    ASTEROID_LIST.update()
    BLAST_LIST.update()

def processCollisions():
    global TOTAL_SCORE
    #asteroids.collide(SHIP)
    collide_list = pygame.sprite.spritecollide(SHIP, ASTEROID_LIST, True)
    for asteroid in collide_list:
        ASTEROID_LIST.remove(asteroid)
        SHIP.damage()

    #blasts.collide(asteroids)
    for blast in BLAST_LIST:
        hit_list = pygame.sprite.spritecollide(blast, ASTEROID_LIST, True)
        for asteroid in hit_list:
            # asteroid splitted
            if (asteroid.type == 0 or asteroid.type == 1):
                new1 = Asteroid(asteroid.type + 1, WIDTH, HEIGHT)
                new1.x, new1.y = asteroid.x, asteroid.y
                ASTEROID_LIST.add(new1)
                new2 = Asteroid(asteroid.type + 1, WIDTH, HEIGHT)
                new2.x, new2.y = asteroid.x, asteroid.y
                ASTEROID_LIST.add(new2)
            ASTEROID_LIST.remove(asteroid)
            BLAST_LIST.remove(blast)
            TOTAL_SCORE += ASTEROID_SCORES[asteroid.type]

        if blast.x > WIDTH or blast.x < 0 or blast.y > HEIGHT or blast.y < 0:
            BLAST_LIST.remove(blast)
        
    if (len(ASTEROID_LIST) == 0):
        for i in range(4):
            asteroid = Asteroid(0, WIDTH, HEIGHT)
            ASTEROID_LIST.add(asteroid)
    
def drawObjects():
    ASTEROID_LIST.draw(WINDOW)
    if (SHIP.lives > 0):
        WINDOW.blit(SHIP.image, SHIP.rect)
    BLAST_LIST.draw(WINDOW)

def displayScore():
    font = pygame.font.SysFont("monospace", 24)
    label = font.render(str(TOTAL_SCORE), 1, (200,200,200))
    WINDOW.blit(label, (50, 10))

def displayShipLivesGameOver():
    rect = SHIP.surface.get_rect()
    if (SHIP.lives >= 1):
        rect.center = (30, 60)
        WINDOW.blit(SHIP.surface, rect)
    if (SHIP.lives >= 2):
        rect.center = (50, 60)
        WINDOW.blit(SHIP.surface, rect)
    if (SHIP.lives >= 3):
        rect.center = (70, 60)
        WINDOW.blit(SHIP.surface, rect)
    if (SHIP.lives == 0):
        font = pygame.font.SysFont("monospace", 36)
        label = font.render("GAME OVER", 1, (200,200,200))
        WINDOW.blit(label, (WIDTH/2-100, HEIGHT/2-50))
    
    pygame.display.update()
    FPS.tick(30)
    
if __name__ == '__main__':
    main()

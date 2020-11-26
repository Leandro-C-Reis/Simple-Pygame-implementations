import pygame as game
import sys
from pygame.locals import *

game.init()

FPS = 30
fpsClock = game.time.Clock()

SURFACE = game.display.set_mode((400, 300))
game.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = game.image.load('./images/cat.png')
catx = 10
caty = 10

direction = 'right'

while True:
    SURFACE.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    SURFACE.blit(catImg, (catx, caty))

    for event in game.event.get():
        if event.type == QUIT or event.type == 768 and event.key == 8:
            game.quit()
            sys.exit()
        if event.type == 768 and event.scancode == 82:
            FPS += 5
        elif event.type == 768 and event.scancode == 81:
            FPS -= 5
            #print(event)

    game.display.update()
    fpsClock.tick(FPS)

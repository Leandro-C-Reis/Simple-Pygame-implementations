import pygame as game
import sys;

from pygame.locals import *

game.init()

SURF_DISPLAY = game.display.set_mode((800, 600))
game.display.set_caption('First draw screen')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Draw

SURF_DISPLAY.fill(WHITE)
ACTUAL_FILL = 'WHITE'

game.draw.polygon(SURF_DISPLAY, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
game.draw.line(SURF_DISPLAY, BLUE, (60, 60), (120, 60), 4)
game.draw.line(SURF_DISPLAY, BLUE, (120, 60), (60, 120))
game.draw.line(SURF_DISPLAY, BLUE, (60, 120), (120, 120), 4)
game.draw.circle(SURF_DISPLAY, RED, (300, 50), 20, 0)
game.draw.ellipse(SURF_DISPLAY, RED, (300, 250, 40, 80), 6)
game.draw.rect(SURF_DISPLAY, BLUE, (200, 150, 100, 50))

pixObj = game.PixelArray(SURF_DISPLAY)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# Game Loop

while True:
    for event in game.event.get():
        if event.type == QUIT or event.type == 768 and event.key == 8:
            game.quit()
            sys.exit()
        if event.type == 768 and event.key == 13:
            if ACTUAL_FILL == 'WHITE':
                SURF_DISPLAY.fill(BLACK)
                ACTUAL_FILL = 'BLACK'
            else:
                SURF_DISPLAY.fill(WHITE)
                ACTUAL_FILL = 'WHITE'
    game.display.update()


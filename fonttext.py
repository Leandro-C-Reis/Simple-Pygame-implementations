import pygame as game
import sys
from pygame.locals import *

game.init()
SURFACE = game.display.set_mode((400, 300))
game.display.set_caption('Text on screen')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Text Render
fontObj = game.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello, World!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

# main Loop
while True:
    SURFACE.fill(WHITE)
    SURFACE.blit(textSurfaceObj, textRectObj)

    for event in game.event.get():
        if event.type == QUIT:
            game.quit()
            sys.exit()
    game.display.update()

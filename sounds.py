import pygame as game
import sys
import time
from pygame.locals import *

game.init()

SURFACE = game.display.set_mode((400, 300))
game.display.set_caption('First Sounds')

soundObj = game.mixer.Sound('./utils/Cue_1.wav')
#music = game.music.play(-1, 0.0)
soundObj.play()
time.sleep(1)
soundObj.stop()

game.quit()
sys.exit()

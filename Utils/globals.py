import pygame as pg
# game constants
SCREENRECT = pg.Rect(0, 0, 1280, 750)
FRAMERATE = 120
SCORE = 0
MAX_SHOTS = 2  # most player bullets onscreen
BOMB_ODDS = 60000/FRAMERATE  # chances a new bomb will drop
ALIEN_RELOAD = 1 # frames between new aliens

dt = 0.0
fullscreen = False
winstyle = 0
screen = None
best_depth = 0
alien_countdown = ALIEN_RELOAD

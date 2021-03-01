import pygame as pg
# game constants
SCREENRECT = pg.Rect(0, 0, 1280, 750)
FRAMERATE = 120
SCORE = 0
MAX_SHOTS = 2  # most player bullets onscreen
BOMB_ODDS = 60000/FRAMERATE  # chances a new bomb will drop
PLATFORM_RELOAD_TIME = 0.1
player_object = None
dt = 0.0
fullscreen = False
winstyle = 0
screen = None
best_depth = 0
platform_countdown = PLATFORM_RELOAD_TIME
screen_speed = [0.0, 0.0]

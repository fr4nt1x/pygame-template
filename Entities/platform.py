import random
import pygame as pg
from Utils import globals


class Platform(pg.sprite.Sprite):
    """ An platform. That slowly moves down the screen.
    """

    default_speed = [globals.SCREENRECT.width * 0.15, 0.0]
    animcycle = max(1, int(1440/globals.FRAMERATE))
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = pg.Surface([globals.SCREENRECT.width * 0.05, globals.SCREENRECT.height*0.02])
        self.image.fill(pg.Color(100,0,0))
        self.rect = self.image.get_rect()
        self.screenrect = pg.Rect(globals.SCREENRECT.x-self.rect.width,
                                  globals.SCREENRECT.y+self.rect.height,
                                  globals.SCREENRECT.width+self.rect.width,
                                  globals.SCREENRECT.height+self.rect.height)

        self.rect.bottom = random.randint(globals.SCREENRECT.y, globals.SCREENRECT.height)
        self.speed = [-(1.0 + random.random()) * Platform.default_speed[0], Platform.default_speed[1]]
        self.frame = 0
        self.rect.right = globals.SCREENRECT.right

    def update(self):
        x = (self.speed[0] + globals.screen_speed[0]) * globals.dt
        y = (self.speed[1] + globals.screen_speed[1]) * globals.dt
        self.rect.move_ip(x, y)
        if not self.screenrect.contains(self.rect):
            self.kill()

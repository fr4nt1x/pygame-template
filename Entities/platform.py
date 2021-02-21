import random

import pygame as pg

from Utils import globals


class Platform(pg.sprite.Sprite):
    """ An platform. That slowly moves down the screen.
    """

    speed = globals.SCREENRECT.width*0.3
    animcycle = max(1, int(1440/globals.FRAMERATE))
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = pg.Surface([200, globals.SCREENRECT.height*0.02])
        self.image.fill(pg.Color(100,0,0))
        self.rect = self.image.get_rect()
        self.screenrect = pg.Rect(globals.SCREENRECT.x-self.rect.width,
                                  globals.SCREENRECT.y+self.rect.height,
                                  globals.SCREENRECT.width+self.rect.width,
                                  globals.SCREENRECT.height+self.rect.height)

        
        self.rect.bottom = random.randint(globals.SCREENRECT.y, globals.SCREENRECT.height)
        self.facing = -(1.0+random.random())*Platform.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = globals.SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing*globals.dt, 0)
        if not self.screenrect.contains(self.rect):
            self.kill()

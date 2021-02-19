import random

import pygame as pg

from Utils import globals


class Enemy(pg.sprite.Sprite):
    """ An alien space ship. That slowly moves down the screen.
    """

    speed = 300
    animcycle = max(1, int(1440/globals.FRAMERATE))
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        
        self.rect.bottom = random.randint(globals.SCREENRECT.y, globals.SCREENRECT.height)
        self.facing = -(1.0+random.random())*Enemy.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = globals.SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing*globals.dt, 0)
        if not globals.SCREENRECT.contains(self.rect):
            self.kill()
        self.frame = self.frame + 1
        self.image = self.images[(self.frame // self.animcycle) % 3]

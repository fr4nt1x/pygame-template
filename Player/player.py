import pygame as pg

from Utils import globals

from Utils.utils import load_image


class Player(pg.sprite.Sprite):
    """ Representing the player as a moon buggy type car.
    """

    speed = 500.0
    bounce = 24
    gun_offset = -11
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=globals.SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, directionx, directiony):
        x = 0
        y = 0
        self.origtop = self.rect.top
        if directionx:
            self.facing = directionx
            x = self.speed*globals.dt*directionx
        if directiony:
            y = self.speed*globals.dt*directiony
        self.rect.move_ip(x, y)
        self.rect = self.rect.clamp(globals.SCREENRECT)
        if directionx < 0:
            self.image = self.images[0]
        elif directionx > 0:
            self.image = self.images[1]
        #self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top

    @staticmethod
    def load_image():
        img = load_image("player1.gif")
        Player.images = [img, pg.transform.flip(img, 1, 0)]
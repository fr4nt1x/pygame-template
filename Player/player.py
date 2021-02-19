import pygame as pg

from Utils import globals

from Utils.utils import load_image


class Player(pg.sprite.Sprite):
    """ Representing the player as a moon buggy type car.
    """

    gravity = 1500.0
    speed = 0.0
    max_speed = 2000.0
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
        self.on_ground = True
        self.accel = 0

    def move(self, jumping=False):

        if self.speed <= self.max_speed:
            self.speed += self.gravity * globals.dt

        if jumping and self.on_ground:
            self.on_ground = False
            self.speed = -1000

        if self.rect.bottom >= globals.SCREENRECT.height:
            self.on_ground = True

        self.rect.move_ip(0, self.speed*globals.dt)
        self.rect = self.rect.clamp(globals.SCREENRECT)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top

    @staticmethod
    def load_image():
        img = load_image("player1.gif")
        Player.images = [img, pg.transform.flip(img, 1, 0)]

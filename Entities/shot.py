import pygame as pg
from Utils import globals


class Shot(pg.sprite.Sprite):
    """ a bullet the Player sprite fires.
    """

    speed = -1100
    images = []

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        """ called every time around the game loop.

        Every tick we move the shot upwards.
        """
        self.rect.move_ip(0, self.speed * globals.dt)
        if self.rect.top <= 0:
            self.kill()
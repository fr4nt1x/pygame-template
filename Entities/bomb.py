import pygame as pg

from Entities.explosion import Explosion
from Utils import globals


class Bomb(pg.sprite.Sprite):
    """ A bomb the aliens drop.
    """

    speed = 200.0
    images = []

    def __init__(self, alien):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=alien.rect.move(0, 5).midbottom)

    def update(self):
        """ called every time around the game loop.

        Every frame we move the sprite 'rect' down.
        When it reaches the bottom we:

        - make an explosion.
        - remove the Bomb.
        """
        self.rect.move_ip(0, self.speed*globals.dt)
        if self.rect.bottom >= globals.SCREENRECT.bottom:
            Explosion(self)
            self.kill()
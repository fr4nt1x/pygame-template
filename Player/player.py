import pygame as pg

from Utils import globals

from Utils.utils import load_image


class Player(pg.sprite.Sprite):
    """ Representing the player as a moon buggy type car.
    """

    gravity = 1500.0
    speed = [0.0, 0.0]
    relative_speed = [0.0, 0.0]
    max_speed = [globals.SCREENRECT.width*0.5, globals.SCREENRECT.height]
    bounce = 24
    gun_offset = -11
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=globals.SCREENRECT.center)
        self.reloading = 0
        self.on_ground = True
        self.can_jump = True

    def move(self, facing=0, jumping=False):
        if self.speed[1] <= self.max_speed[1]:
            self.speed[1] += self.gravity * globals.dt
        
        if jumping and self.on_ground and self.can_jump:
            self.on_ground = False
            self.speed[1] = -self.max_speed[1]
            self.can_jump = False
        elif not jumping:
            self.can_jump = True
        self.speed[0] = facing * self.max_speed[0]

        self.rect.move_ip((self.speed[0]+self.relative_speed[0]+globals.screen_speed[0])*globals.dt,
                          (self.speed[1]+self.relative_speed[1]+globals.screen_speed[1])*globals.dt)

        if self.rect.bottom > globals.SCREENRECT.bottom:
            self.rect.bottom = globals.SCREENRECT.bottom 
            self.on_ground = True

        if self.rect.right > globals.SCREENRECT.right:
            self.rect.right = globals.SCREENRECT.right
        elif self.rect.left < globals.SCREENRECT.left:
            self.rect.left = globals.SCREENRECT.left

    @staticmethod
    def load_image():
        img = load_image("player1.gif")
        Player.images = [pg.transform.scale(img, (int(0.05*globals.SCREENRECT.width), int(0.05*globals.SCREENRECT.height)))]

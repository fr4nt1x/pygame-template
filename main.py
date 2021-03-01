#!/usr/bin/env python
""" pygame.examples.aliens

Shows a mini game where you have to defend against aliens.

What does it show you about pygame?

* pg.sprite, the difference between Sprite and Group.
* dirty rectangle optimization for processing for speed.
* music with pg.mixer.music, including fadeout
* sound effects with pg.Sound
* event processing, keyboard handling, QUIT handling.
* a main loop frame limited with a game clock from pg.time.Clock
* fullscreen switching.


Controls
--------

* Left and right arrows to move.
* Space bar to shoot
* f key to toggle between fullscreen.

"""

import random
import os

# import basic pygame modules
import pygame as pg

# see if we can load more than standard BMP
from Utils import globals
from Entities.platform import Platform

from Player.player import Player
from Utils.score import Score
from Entities.shot import Shot
from Utils.utils import load_image, load_sound
if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

def main(winstyle=0):
    # Initialize pygame
    initiate_pygame()

    load_all_images()

    # decorate the game window
    icon = pg.transform.scale(Platform.images[0], (32, 32))
    pg.display.set_icon(icon)
    pg.display.set_caption("Pygame Aliens")
    pg.mouse.set_visible(0)

    background = initiate_background()

    # load the sound effects
    boom_sound = load_sound("boom.wav")
    shoot_sound = load_sound("car_door.wav")
    if pg.mixer:
        pass
        # music = os.path.join(get_data_dir(), "house_lo.wav")
        # pg.mixer.music.load(music)
        # pg.mixer.music.play(-1)

    platforms, all, bombs, lastalien, shots = initiate_containers()

    # Create Some Starting Values
    clock = pg.time.Clock()

    # initialize our starting sprites
    globals.player_object = Player()
    Platform()  # note, this 'lives' because it goes into a sprite group
    if pg.font:
        all.add(Score())

    # Run our main loop whilst the player is alive.
    while globals.player_object.alive():

        # get input

        if handle_events():
            return

        keystate = pg.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(globals.screen, background)

        # update all the sprites
        all.update()

        globals.platform_countdown -= globals.dt
        if globals.platform_countdown <= 0:
            globals.platform_countdown = random.random() + globals.PLATFORM_RELOAD_TIME
            Platform()

        # Detect collisions between platform and players.
        globals.player_object.relative_speed[0] = 0.0
        for platform in pg.sprite.spritecollide(globals.player_object, platforms, 0):
            globals.player_object.on_ground = True
            globals.player_object.speed[1] = 0
            globals.player_object.relative_speed[0] = platform.speed[0]
            globals.player_object.rect.bottom = platform.rect.top

        # handle player input
        jumping = keystate[pg.K_SPACE]

        right = keystate[pg.K_RIGHT]
        left = -1*keystate[pg.K_LEFT]

        if globals.player_object.rect.right >= (globals.SCREENRECT.width)/3:
            globals.screen_speed[0] = -900
        else:
            globals.screen_speed[0] = 0
        #elif globals.player_object.rect.right < (globals.SCREENRECT.width)/3:
           # globals.screen_speed[0] = 0
        globals.player_object.move(right+left, jumping)


            # draw the scene
        dirty = all.draw(globals.screen)
        pg.display.update(dirty)

        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        globals.dt = clock.tick(globals.FRAMERATE)/1000.0
    if pg.mixer:
        pg.mixer.music.fadeout(1000)
    pg.time.wait(1000)
    pg.quit()


def handle_events():
    exit_game = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game = True
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            exit_game = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                if not globals.fullscreen:
                    print("Changing to FULLSCREEN")
                    screen_backup = globals.screen.copy()
                    globals.screen = pg.display.set_mode(
                        globals.SCREENRECT.size, globals.winstyle | pg.FULLSCREEN, globals.bestdepth
                    )
                    globals.screen.blit(screen_backup, (0, 0))
                else:
                    print("Changing to windowed mode")
                    screen_backup = globals.screen.copy()
                    globals.screen = pg.display.set_mode(
                        globals.SCREENRECT.size, globals.winstyle, globals.bestdepth
                    )
                    globals.screen.blit(screen_backup, (0, 0))
                pg.display.flip()
                globals.fullscreen = not globals.fullscreen
    return exit_game


def initiate_background():
    # create the background, tile the bgd image
    #bgdtile = load_image("background.gif")
    bgdtile = pg.Surface([globals.SCREENRECT.width, globals.SCREENRECT.height])
    bgdtile.fill(pg.Color(0, 50, 100))
    background = pg.Surface(globals.SCREENRECT.size)
    pg.transform.scale(bgdtile, globals.SCREENRECT.size, background)
    globals.screen.blit(background, (0, 0))
    pg.display.flip()
    return background


def initiate_pygame():
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()
    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None
    pg.mixer.music.set_volume(0.1)
    globals.fullscreen = False
    # Set the display mode
    globals.winstyle = 0  # |FULLSCREEN
    globals.bestdepth = pg.display.mode_ok(globals.SCREENRECT.size, globals.winstyle, 64)
    globals.screen = pg.display.set_mode(globals.SCREENRECT.size, globals.winstyle, globals.bestdepth)


def initiate_containers():
    # Initialize Game Groups
    platforms = pg.sprite.Group()
    shots = pg.sprite.Group()
    bombs = pg.sprite.Group()
    all = pg.sprite.RenderUpdates()
    lastalien = pg.sprite.GroupSingle()
    # assign default groups to each sprite class
    Player.containers = all
    Platform.containers = platforms, all, lastalien
    Shot.containers = shots, all
    Score.containers = all
    return platforms, all, bombs, lastalien, shots


def load_all_images():
    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    Player.load_image()
    Platform.images = [load_image(im) for im in ("alien1.gif", "alien2.gif", "alien3.gif")]
    Shot.images = [load_image("shot.gif")]


# call the "main" function if running this script
if __name__ == "__main__":
    main()

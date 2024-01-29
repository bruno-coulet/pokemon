# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: generic.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from pygamevideo import Video


class Generic:
    def __init__(self):
        self.generic = Video('assets/videos/intro_clip.mp4')
        self.pause = False

    def play(self):
        pg.display.set_mode((1024, 768), 0, 0, 0, 0)
        self.generic.play(loop=True)

        runner = True
        while runner:
            clock.tick(FPS)
            events = pg.event.get()
            self.generic.draw_to(SCREEN, (0, 0))

            for event in events:
                if event.type == pg.QUIT:
                    self.generic.stop()
                    runner = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.generic.stop()
                        runner = False
                    if event.key == pg.K_DELETE:
                        self.generic.stop()
                        runner = False

            pg.display.flip()
        pg.display.set_mode(DSP_SIZE, 0, 0, 0, 0)

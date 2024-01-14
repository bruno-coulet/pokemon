#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET, Cyril GENISSON
@file: map.py

@project: Pokémon
@licence: GPLv3
"""

from constants import DSP_WIDTH, DSP_HEIGHT
import random
import pygame as pg


class Map(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_size = 258, 146
        self.img_width, self.img_height = self.img_size
        self.sprite_sheet = pg.image.load('assets/images/battle.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.images = {
            'map_1': self.get_image(1, 1),
            'map_2': self.get_image(259, 1),
            'map_3': self.get_image(516, 1),
            'map_4': self.get_image(1, 147),
            'map_5': self.get_image(259, 147),
            'map_6': self.get_image(516, 147),
            'map_7': self.get_image(1, 293),
            'map_8': self.get_image(259, 293),
            'map_9': self.get_image(516, 293),
            'map_10': self.get_image(1, 438),
            'map_11': self.get_image(259, 438)
        }

        self.map_list = [f'map_{k}' for k in range(1, 12)]
        self.random_map(random.choice(self.map_list))

    def random_map(self, name):
        self.image = self.images[name]
    
    def get_image(self, x, y):
        full_screen = pg.Surface([DSP_WIDTH, DSP_HEIGHT])
        sprite_image = pg.Surface(self.img_size)
        sprite_image.blit(self.sprite_sheet, (0, 0), (x, y, self.img_width, self.img_height))
        pg.transform.scale(sprite_image, (DSP_WIDTH, DSP_HEIGHT), full_screen)
        return full_screen

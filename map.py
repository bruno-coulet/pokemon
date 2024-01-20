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
        # self.sprite_sheet = pg.image.load('assets/images/pokemon_map.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.images = {
            'map_1': self.get_image(               1, 1),
            'map_2': self.get_image(self.img_width+1, 1),
            'map_3': self.get_image(self.img_width*2, 1),
            'map_4': self.get_image(               1, self.img_height+1),
            'map_5': self.get_image(self.img_width+1, self.img_height+1),
            'map_6': self.get_image(self.img_width*2, self.img_height+1),
            'map_7': self.get_image(               1, self.img_height+1),
            'map_8': self.get_image(self.img_width+1, self.img_height+1),
            'map_9': self.get_image(self.img_width*2, self.img_height+1),
            'map_10': self.get_image(1, self.img_height*3),
            'map_11': self.get_image(self.img_width+1, self.img_height*3)
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

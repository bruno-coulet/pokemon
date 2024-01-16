#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON, Bruno COULET
@file: constants.py

@project: Pokémon
@licence: GPLv3
"""
import pygame as pg

ABOUT = [f'POKEMON BATTLE CLONE',
         f'Version: 0.1',
         f'Bruno COULET',
         f'Ugo D\'AMBROSIO',
         f'Cyril GENISSON',
         ]


COLORS = {'BLACK': (0, 0, 0),
          'WHITE': (255, 255, 255),
          'RED': (255, 0, 0),
          'DARK_RED':(170,15,10),
          'GREEN': (0, 255, 0),
          'BLUE': (0, 0, 255),
          'DARK_BLUE':(37,47,135),
          'YELLOW': (255, 255, 0),
          'CYAN': (0, 255, 255),
          'MAGENTA': (255, 0, 255),
          'GREY' : (12, 25, 29),
          'CREME' : (240,240,240)}

#
# DISPLAY
#
DSP_WIDTH = 800
DSP_HEIGHT = 600
FPS = 80
SCREEN = pg.display.set_mode((DSP_WIDTH, DSP_HEIGHT), 0, 0, 0, 0)
pg.display.set_caption("Pokemon Battle Clone")
ico = pg.image.load('assets/images/Pokeball_icon.svg')
pg.display.set_icon(ico)
clock = pg.time.Clock()


#
# BUTTONS
#



#
# MENU
#
MENU_WIDTH = DSP_WIDTH * 0.75
MENU_HEIGHT = DSP_HEIGHT * 0.75

#
# POKEDEX
#
POKEDEX_FILE = 'pokedex/pokedex.json'
POKEDEX_SAVE_PATH = './save/'

#
# POKEMONS AND TYPES SPRITES PATH
#
SP_POK_PATH = './assets/datas/sprites/Pokemons/'
SP_TYP_PATH = './assets/datas/sprites/Types/'

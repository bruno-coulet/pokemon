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
         # f'Ugo D\'AMBROSIO',
         f'Cyril GENISSON',
         ]


COLORS = {'BLACK': (0, 0, 0),
          'WHITE': (255, 255, 255),
          'RED': (255, 0, 0),
          'DARK_RED': (170, 15, 10),
          'GREEN': (0, 255, 0),
          'LIGHT_BLUE': (80, 100, 200),
          'BLUE': (0, 0, 255),
          'ORANGE': (215, 165, 55),
          'DARK_BLUE': (25, 35, 100),
          'YELLOW': (255, 255, 0),
          'TRANSPARENT_YELLOW': (255, 255, 0, 150),
          'CYAN': (0, 255, 255),
          'MAGENTA': (255, 0, 255),
          'GREY': (12, 25, 29),
          'CREME': (240, 240, 240),
          'TRANSPARENT_CREME': (240, 240, 240, 150),
          'TRANSPARENT_BLACK': (0, 0, 0, 150),
          'TRANSPARENT_RED':(200, 0, 0, 150),
          'TRANSPARENT_GREEN':(0, 200, 0, 150),
          'HOVER_COLOR': (100, 200, 100),
          }

#
# DISPLAY
#
DSP_WIDTH = 800
DSP_HEIGHT = 600
# DSP_WIDTH =1024
# DSP_HEIGHT = 768
DSP_SIZE = (DSP_WIDTH, DSP_HEIGHT)
FPS = 60
SCREEN = pg.display.set_mode(DSP_SIZE, 0, 0, 0, 0)
pg.display.set_caption("Pokemon Battle Clone")
ico = pg.image.load('assets/images/Pokeball_icon.svg')
pg.display.set_icon(ico)
clock = pg.time.Clock()


#
# FONTS
#
KANIT = 'assets/fonts/kanit_medium.ttf'
KANIT_BOLD = 'assets/fonts/kanit_extraboldItalic.ttf'
MARHEY = 'assets/fonts/marhey.ttf'


#
# MENU
#
MENU_WIDTH = DSP_WIDTH * 0.75
MENU_HEIGHT = DSP_HEIGHT * 0.75

#
# POKEDEX
#
POKEDEX_FILE = 'pokedex/pokedex.json'
POKEDEX_SAVE = './save/save.json'

#
# POKEMONS AND TYPES SPRITES PATH
#
SP_POK_PATH = 'assets/datas/sprites/Pokemons/'
SP_TYP_PATH = 'assets/datas/sprites/Types/'



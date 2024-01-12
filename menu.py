#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: menu.py

@project: Pokémon
@licence: GPLv3
"""
import pygame_menu as pgm
from constants import *


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.user = 'Sacha'

        self.menu_theme = pgm.themes.THEME_DARK.copy()
        self.menu_theme.title_background_color = (10, 10, 10, 255)
        self.menu_theme.background_color = (0, 0, 0, 255)
        self.menu_theme.title_font_color = COLORS['YELLOW']
        self.menu_theme.title_font_size = 40
        self.menu_theme.text_font_size = 30
        self.menu_theme.text_color = COLORS['YELLOW']
        self.menu_theme.text_font_color = ['YELLOW']
        self.menu_theme.title_close_button = True
        self.menu_theme.text_align = 'center'

        self.menu_pokedex = pgm.Menu("Pokedex", self.width, self.height, True, theme=self.menu_theme)
        self.menu_restore = pgm.Menu("Restore save", self.width, self.height, True, theme=self.menu_theme)

        self.about_menu = pgm.Menu('About', self.width, self.height, True, theme=self.menu_theme)
        for m in ABOUT:
            self.about_menu.add.label(m, align=pgm.locals.ALIGN_CENTER, font_size=40, font_color=COLORS['YELLOW'])
        self.about_menu.add.vertical_margin(30)
        self.about_menu.add.button('Return to menu', pgm.events.BACK)

        self.main_menu = pgm.Menu("Pokémon", self.width, self.height, True, theme=self.menu_theme)
        self.main_menu.add.text_input('User: ', default="Sacha", maxchar=20, font='arial', textinput_id='user')
        self.main_menu.add.vertical_margin(10)
        self.main_menu.add.button('Start new game', self.play_game)
        self.main_menu.add.vertical_margin(10)
        self.main_menu.add.button('Restore last save', self.menu_restore)
        self.main_menu.add.vertical_margin(10)
        self.main_menu.add.button('Add a Pokemon', self.menu_pokedex)
        self.main_menu.add.vertical_margin(10)
        self.main_menu.add.button('About', self.about_menu)
        self.main_menu.add.vertical_margin(10)
        self.main_menu.add.button('Quit', self.quit)

    def play_game(self):
        pass

    def quit(self):
        pass

    def see_pokedex(self):
        pass

    def restore_save(self):
        pass

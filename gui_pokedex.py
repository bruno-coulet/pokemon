#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET
@file: gui_pokedex.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from gui_battle import *
from button import *
from map import Map
import pygame as pg
import os
from random import randint

TRANSPARENT_BLACK = (0,0,0,200)

MENU_BTN_WIDTH = 120
MENU_BTN_HEIGHT = 50

PREV_BTN_X = 60
PREV_BTN_Y = 480

NEXT_BTN_X = 260
NEXT_BTN_Y = 480

VALID_BTN_X = 460
VALID_BTN_Y = 480

BACK_BTN_X = 630
BACK_BTN_Y = 480

""" IL FAUT Créer une variable current_pokemon pour pouvoir les afficher un à un.
    probablement ajouter cette variable aux paramètre de la classe GuiPokedex

dex.add_pokemon(current_pokemon)
pok1 = Pokemon(dex.get_pokemon(current_pokemon))

"""

class GuiPokedex(Pokedex):

    def __init__(self, choose_pokemon_title, x, y, width, height, pok_type ):
        pg.font.init()
        self.FONT = pg.font.Font(KANIT, 18)
        self.title = choose_pokemon_title
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pok_type = pok_type

    def draw(self, screen):
        # crée une surface qui gère la transparence
        description_background = pg.Surface((self.width, self.height), pg.SRCALPHA)
        # crée la surface dans un rectangle
        pg.draw.rect(description_background, TRANSPARENT_BLACK, (0, 0, self.width, self.height), border_radius=20)
        # affiche la surface
        screen.blit(description_background, (self.x, self.y))
        #  crée un text de description
        description_text = self.FONT.render(self.title, True, (COLORS['WHITE']))
        text_rect = description_text.get_rect(center=(self.x + self.width // 2, self.y + self.height - 20))
        # affiche le texte de description
        screen.blit(description_text, text_rect)

class MenuButton(Button):
    def __init__(self, color, btn_text, x, y, width, height, pok_type):
        super().__init__(btn_text, x, y, width, height, pok_type)
        self.color = color

if __name__ == "__main__":
    pg.init()
    # dex = Pokedex()
    
    menu_background = Map()

    choose_pokemon = GuiPokedex("current Pokemon", 30, 60, 512*3/4, 512*3/4, "pok_type")
    pokemon_description = GuiPokedex("Pokemon description", (DSP_WIDTH - 350 - 30), 60, 350, 512*3/4, "pok_type")

    previous_btn = MenuButton(btn_text = "Suivant", color = COLORS['RED'], x = PREV_BTN_X, y = PREV_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = 'atk_method')
    next_btn = MenuButton(btn_text = "Précedent", color = COLORS['DARK_RED'], x = NEXT_BTN_X, y = NEXT_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = 'spe_atk')
    select_btn = MenuButton(btn_text = "Valider", color = COLORS['LIGHT_BLUE'], x = VALID_BTN_X, y = VALID_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = '___')
    back_btn = MenuButton(btn_text = "Retour", color = COLORS['DARK_BLUE'], x = BACK_BTN_X, y = BACK_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = '___')

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        SCREEN.blit(menu_background.image, menu_background.rect)
        choose_pokemon.draw(SCREEN)
        pokemon_description.draw(SCREEN)
        previous_btn.draw(SCREEN)
        next_btn.draw(SCREEN)
        select_btn.draw(SCREEN)
        back_btn.draw(SCREEN)

        pg.display.flip()

    pg.quit()
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
from pokedex import Pokedex

TRANSPARENT_BLACK = (0,0,0,200)
HOVER_COLOR = (100, 200, 100)

pg.font.init()
FONT_1 = pg.font.Font(MARHEY, 18)
FONT_2 =  pg.font.Font(KANIT, 18)

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

    def __init__(self, title, text, x, y, width, height ):
        # pg.font.init()
        self.FONT = FONT_1
        self.title = title
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.pok_type = pok_type
    #  Rectangles gris
    def draw_area(self, screen):
        # crée une surface qui gère la transparence
        description_background = pg.Surface((self.width, self.height), pg.SRCALPHA)
        # crée la surface dans un rectangle
        pg.draw.rect(description_background, TRANSPARENT_BLACK, (0, 0, self.width, self.height), border_radius=20)
        # affiche la surface
        screen.blit(description_background, (self.x, self.y))

    def draw_title(self, screen):
        #  crée un titre de description
        description_title = self.FONT.render(self.title, True, (COLORS['WHITE']))
        text_rect = description_title.get_rect(center=(self.x + self.width // 2, self.y+20))
        # affiche le titre de description
        screen.blit(description_title, text_rect)
    
    def draw_icon(self, screen):
        # Charger l'icône et crée la surface
        icon_path = "assets/datas/sprites/Types/Plante.png"
        icon_surface = pg.image.load(icon_path).convert_alpha()
        # Afficher l'icône
        screen.blit(icon_surface, (self.x+self.width//2-30, self.y+50))

    def draw_description_text(self, screen):
        # Encore une zone gris transparent en fond
        description_background = pg.Surface((self.width, self.height), pg.SRCALPHA)
        pg.draw.rect(description_background, TRANSPARENT_BLACK, (10, 120, self.width-20, self.height-130), border_radius=20)
        screen.blit(description_background, (self.x, self.y))

        #  crée le texte de description
        # La méthode render prend le texte, un booléen pour l'antialiasing, et la couleur du texte en RGB.
        description_text = self.FONT.render(self.text, True, (COLORS['WHITE']))
        text_rect = description_text.get_rect(topleft=(self.x + 20, self.y + 150) )
        # affiche le texte de description
        screen.blit(description_text, text_rect)

    def draw_picture(sefl, screen):
        # Charger l'image et crée la surface
        icon_path = "assets/datas/sprites/Pokemons/1-regular.png"
        icon_surface = pg.image.load(icon_path).convert_alpha()
        # Redimensionne l'image à la taille souhaitée
        resized_icon = pg.transform.scale(icon_surface, (300, 300))
        # Affiche l'image sur l'écran
        screen.blit(resized_icon, (80,100))

class CurrentPokemon(Pokedex):
    def __init__(self, title, text, x, y, width, height, pok_type, pok_id, pok_name, pok_sprite, pok_description ):
        
        Pokedex.__init__(self, title, text, x, y, width, height, pok_type)
        self.pok_id = pok_id
        self.pok_name = pok_name
        self.pok_sprite = pok_sprite
        self.pok_type = pok_type
        self.pok_description = pok_description
        
    def get_pok_id(self, screen):
        pok_id = pok_data[0]['pokedexId']
        pok_sprite = pok_data[0]['sprites']['regular']

class MenuButton(Button):
    def __init__(self, color, btn_text, x, y, width, height, pok_type):
        super().__init__(btn_text, x, y, width, height, pok_type)
        self.color = color
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, screen):
        mx, my = pg.mouse.get_pos()

        if self.rect.collidepoint(mx, my):  # Use the collidepoint method on the instance
            pg.draw.rect(screen, HOVER_COLOR, self, border_radius=10)
        else:
            pg.draw.rect(screen, self.color, self, border_radius=10)

        # Réaffiche le texte des boutons qui avait disparu
        text = FONT_1.render(self.btn_text, True, COLORS['WHITE'])  # Assuming COLORS is defined somewhere
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
    
class NavButton(Button):
    def __init__(self, color, btn_text, x, y, width, height, pok_type):
        super().__init__(btn_text, x, y, width, height, pok_type)
        self.color = color
        self.points = [(x, y+25), (x + 100, y), (x + 100, y + 50) ]
        self.hover_points = [(x-4, y+25), (x + 104, y-4), (x + 104, y + 54) ]
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, screen):
        mx, my = pg.mouse.get_pos()

        if self.rect.collidepoint(mx, my):
            pg.draw.polygon(screen, HOVER_COLOR,self.hover_points)
            pg.draw.polygon(screen, self.color, self.points)
        else:
            pg.draw.polygon(screen, self.color, self.points)

        # affiche le texte des boutons
        text = FONT_1.render(self.btn_text, True, COLORS['WHITE'])
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)


if __name__ == "__main__":
    pg.init()
    # dex = Pokedex()

    menu_background = Map()

    choose_pokemon = GuiPokedex("current Pokemon", None, 30, 60, 512*3/4, 512*3/4)
    pokemon_description = GuiPokedex("Pokemon description", "texte de description bla bla blabnùbinetbùetnbettbnetpbneùpneùn", (DSP_WIDTH - 350 - 30), 60, 350, 512*3/4)

    previous_btn = NavButton(btn_text = "Précedent", color = COLORS['RED'], x = PREV_BTN_X, y = PREV_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = 'atk_method')
    next_btn = NavButton(btn_text = "Suivant", color = COLORS['DARK_RED'], x = NEXT_BTN_X, y = NEXT_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = 'spe_atk')
    select_btn = MenuButton(btn_text = "Valider", color = COLORS['LIGHT_BLUE'], x = VALID_BTN_X, y = VALID_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = '___')
    back_btn = MenuButton(btn_text = "Retour", color = COLORS['DARK_BLUE'], x = BACK_BTN_X, y = BACK_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = '___')

    run = True
    while run:
    
        mx, my = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # clic
                pos = event.pos

        # Affiche le fond
        SCREEN.blit(menu_background.image, menu_background.rect)

        # Zone portrait du pokemon a gauche
        choose_pokemon.draw_area(SCREEN)
        choose_pokemon.draw_title(SCREEN)
        choose_pokemon.draw_picture(SCREEN)
        # Zone description du pokemon a droite
        pokemon_description.draw_area(SCREEN)
        pokemon_description.draw_title(SCREEN)
        pokemon_description.draw_icon(SCREEN)
        pokemon_description.draw_description_text(SCREEN)
        # Boutons en bas
        previous_btn.draw(SCREEN)
        next_btn.draw(SCREEN)
        select_btn.draw(SCREEN)
        back_btn.draw(SCREEN)
        # ...

        pg.display.flip()

    pg.quit()
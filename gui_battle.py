#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET
@file: gui_battle.py

@project: Pokémon
@licence: GPLv3
"""

from constants import *
from battle import *
from map import Map
import pygame as pg

"""La class Gui_battle doit avoir toutes les méthodes pour gérer l'affichage des différents éléments:
    - les 2 sprite des 2 pokémons
    - leur barre hp progressant au cours des attaques,
    - les boutons avec la gestion de la souris ou du clavier pour les différents choix:
    - attaque
    - attaque spéciale
    - fuite
    - changer de pokémon.
    
    Enfin il faudra une méthode spéciale pour afficher un  texte de quelques mots au milieu ou alors dans un encart de l'écran pour suivre les différentes actions.
"""
class Gui_battle:
    def __init__(self):
        pg.init()        

        # Charger les sprites des deux Pokémon
        self.pokemon1_sprite = pg.image.load("assets/datas/sprites/Pokemons/1-regular.png")#json_data[id_pok]['sprites']['regular']
        self.pokemon2_sprite = pg.image.load("assets/datas/sprites/Pokemons/1-regular.png")

    def draw_pokemon_sprite(self, screen, x, y):
        screen.blit(self.pokemon1_sprite, (x, y))

        # Définir la position initiale des éléments
        self.pokemon1_position = (100, 400)
        self.pokemon2_position = (550, 100)
        self.hp_bar_position = (100, 50)

    def display_pokemon_sprites(self):
        # Afficher les sprites des deux Pokémon
        self.screen.blit(self.pokemon1_sprite, self.pokemon1_position)
        self.screen.blit(self.pokemon2_sprite, self.pokemon2_position)

# -----------   a-modifer début   -------------------
    def position_sprite(self, x, y):
        full_screen = pg.Surface([DSP_WIDTH, DSP_HEIGHT])
        sprite_image = pg.Surface(self.img_size)
        sprite_image.blit(self.sprite_sheet, (0, 0), (x, y, self.img_width, self.img_height))
        pg.transform.scale(sprite_image, (DSP_WIDTH, DSP_HEIGHT), full_screen)
        return full_screen
# ----------    a-modifer fin   -------------------
    



if __name__ == "__main__":
    battle_gui = Gui_battle()
    battle_gui.run_battle()



    # def display_hp_bars(self, hp_percentage_pokemon1, hp_percentage_pokemon2):
    #     # Afficher les barres de HP en fonction du pourcentage de HP restant
    #     self.screen.blit(self.hp_bar_sprite, self.hp_bar_position)

    #     # Dessiner la barre de HP pour le Pokémon 1
    #     pg.draw.rect(self.screen, (0, 255, 0), (self.hp_bar_position[0] + 10, self.hp_bar_position[1] + 10,
    #                                             hp_percentage_pokemon1 * 2, 10))

    #     # Dessiner la barre de HP pour le Pokémon 2
    #     pg.draw.rect(self.screen, (0, 255, 0), (self.hp_bar_position[0] + 400, self.hp_bar_position[1] + 10,
    #                                             hp_percentage_pokemon2 * 2, 10))

    # def display_text(self, text):
    #     # Afficher du texte au milieu de l'écran
    #     font = pg.font.Font(None, 36)
    #     text_render = font.render(text, True, (255, 255, 255))
    #     text_rect = text_render.get_rect(center=(400, 300))
    #     self.screen.blit(text_render, text_rect)

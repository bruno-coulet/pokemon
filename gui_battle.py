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
    FAIT    - les 2 sprite des 2 pokémons
    A FAIRE - leur barre hp progressant au cours des attaques,
    - les boutons avec la gestion de la souris ou du clavier pour les différents choix:
    - attaque
    - attaque spéciale
    - fuite
    - changer de pokémon.
    
    Enfin il faudra une méthode spéciale pour afficher un  texte de quelques mots au milieu ou alors dans un encart de l'écran pour suivre les différentes actions.
"""
POK_1_HEIGHT = 300
POK_1_WIDTH = 300
POK_1_x = 50
POK_1_y = 290

POK_2_HEIGHT = 250
POK_2_WIDTH = 250
POK_2_x = 455
POK_2_y = 125


class Gui_battle:
    def __init__(self):
        pg.init()        

        # Charger les sprites des deux Pokémon
        self.pokemon1_sprite = pg.image.load("assets/datas/sprites/Pokemons/1-regular.png")#json_data[id_pok]['sprites']['regular']
        self.pokemon2_sprite = pg.image.load("assets/datas/sprites/Pokemons/2-regular.png")

    # Dessine pokemon joueur
    def draw_pokemon_1_sprite(self, screen):
        screen.blit(pg.transform.scale(self.pokemon1_sprite, (POK_1_HEIGHT, POK_1_WIDTH)), (POK_1_x, POK_1_y))
    # Et le fond de barre
    def draw_pokemon_1_bar(self, screen):
        rectangle_position = (POK_1_x,(POK_1_y))
        rectangle_dimensions = (205, 25)
        rectangle_color = COLORS["RED"]
        pg.draw.rect(screen, rectangle_color, ((rectangle_position[0]-2), (rectangle_position[1]-2), rectangle_dimensions[0], rectangle_dimensions[1]))
    #  et sa barre de vie
    def draw_pokemon_1_life(self, screen):
        rectangle_position = (POK_1_x,(POK_1_y))
        rectangle_dimensions = (200, 20)
        rectangle_color = COLORS["GREEN"]
        pg.draw.rect(screen, rectangle_color, (rectangle_position[0], rectangle_position[1], rectangle_dimensions[0], rectangle_dimensions[1]))
    


    # Dessine pokemon adversaire
    def draw_pokemon_2_sprite(self, screen):
        screen.blit(pg.transform.scale(self.pokemon2_sprite, (POK_2_HEIGHT, POK_2_WIDTH)), (POK_2_x, POK_2_y))
     # Et le fond de barre de vie
    def draw_pokemon_2_bar(self, screen):
        rectangle_position = (POK_1_x,(POK_1_y))
        rectangle_dimensions = (205, 25)
        rectangle_color = COLORS["RED"]
        pg.draw.rect(screen, rectangle_color, ((rectangle_position[0]-2), (rectangle_position[1]-2), rectangle_dimensions[0], rectangle_dimensions[1]))
    #  et sa barre de vie
    def draw_pokemon_2_life(self, screen):
        rectangle_position = (POK_2_x,(POK_2_y))
        rectangle_dimensions = (200, 20)
        rectangle_color = COLORS["GREEN"]
        pg.draw.rect(screen, rectangle_color, (rectangle_position[0], rectangle_position[1], rectangle_dimensions[0], rectangle_dimensions[1]))

if __name__ == "__main__":
    battle_gui = Gui_battle()
    # battle_gui.run_battle()

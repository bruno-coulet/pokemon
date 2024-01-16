#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET, Cyril GENISSON
@file: gui_battle.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from battle import *
from map import Map
import pygame as pg
import os
from random import randint
"""
    A faire:
    - les boutons avec la gestion de la souris ou du clavier pour les différents choix:
    - attaque
    - attaque spéciale
    - fuite
    - changer de pokémon.
    
    Enfin il faudra une méthode spéciale pour afficher un  texte de quelques mots au milieu ou alors dans un encart de
    l'écran pour suivre les différentes actions.
"""
POK_1_HEIGHT = 300
POK_1_WIDTH = 300
POK1_DIMS = (300, 300)
POK2_DIMS = (250, 250)
POK_1_x = 50
POK_1_y = 290

POK_2_HEIGHT = 250
POK_2_WIDTH = 250
POK_2_x = 455
POK_2_y = 125


class GuiBattle(Battle):
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon, pokedex: Pokedex):
        super().__init__(pokemon1, pokemon2, pokedex)
        # Charger les sprites des deux Pokémon
        self.__p1_sprites = [pg.image.load(f"{SP_POK_PATH}{self.p1.id_pok}-regular.png")]
        if os.path.isfile(f'{SP_POK_PATH}{self.p1.id_pok}-shiny.png'):
            self.__p1_sprites.append(pg.image.load(f"{SP_POK_PATH}{self.p1.id_pok}-shiny.png"))
        self.__p2_sprites = [pg.image.load(f"{SP_POK_PATH}{self.p2.id_pok}-regular.png")]
        if os.path.isfile(f'{SP_POK_PATH}{self.p2.id_pok}-shiny.png'):
            self.__p2_sprites.append(pg.image.load(f"{SP_POK_PATH}{self.p2.id_pok}-shiny.png"))

    def draw_p1(self, screen, k):
        screen.blit(pg.transform.scale(self.__p1_sprites[k], size=POK1_DIMS), (POK_1_x, POK_1_y))

    def draw_p2(self, screen, k):
        screen.blit(pg.transform.scale(self.__p2_sprites[k], size=POK2_DIMS), (POK_2_x, POK_2_y))

    def draw_bar(self, screen):
        hp1, hp2 = self.damage_bar()
        rect_dims = [(254, 10), [250 * hp1, 6], [250 * hp2, 6]]

        rec_ini = (POK_1_x, POK_1_y)
        pg.draw.rect(screen, COLORS["RED"], ((rec_ini[0] - 2), (rec_ini[1] - 2), rect_dims[0][0], rect_dims[0][1]),
                     border_radius=20)
        pg.draw.rect(screen, COLORS["GREEN"], (rec_ini[0], rec_ini[1], rect_dims[1][0], rect_dims[1][1]),
                     border_radius=20)

        rec_ini = (POK_2_x, POK_2_y)
        pg.draw.rect(screen, COLORS["RED"], ((rec_ini[0] - 2), (rec_ini[1] - 2), rect_dims[0][0], rect_dims[0][1]),
                     border_radius=20)
        pg.draw.rect(screen, COLORS["GREEN"], (rec_ini[0], rec_ini[1], rect_dims[2][0], rect_dims[2][1]),
                     border_radius=20)


if __name__ == "__main__":
    pg.init()
    dex = Pokedex()
    dex.add_pokemon(1)
    dex.add_pokemon(2)
    pok1 = Pokemon(dex.get_pokemon(1))
    pok2 = Pokemon(dex.get_pokemon(2))
    battle = GuiBattle(pok1, pok2, dex)
    map1 = Map()

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            SCREEN.blit(map1.image, map1.rect)
            battle.draw_bar(SCREEN)
            battle.draw_p1(SCREEN, k=0)
            battle.draw_p2(SCREEN, k=0)
            # for i in [1, 0] * 2:
            #    battle.draw_p1(SCREEN, k=i)
            #    pg.display.flip()
            #    pg.time.delay(250)

            pg.display.flip()

    pg.quit()

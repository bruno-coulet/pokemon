#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET, Cyril GENISSON
@file: gui_battle.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from math import sqrt, log
from battle import Battle
from pokemon import Pokemon
from pokedex import Pokedex
from but import Button
from gui_dex import GuiDex
from map import Map
import pygame as pg
import time
from random import random, randint, choice
import os

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


""" Méthode spéciale pour afficher un  texte de quelques mots au milieu ou alors dans un encart de
    l'écran pour suivre les différentes actions."""
pg.font.init()
police = pg.font.Font(KANIT, 36)
def creer_texte_avec_fond(texte, police, couleur_texte, couleur_fond):
    texte_surface = police.render(texte, True, couleur_texte)
    largeur = texte_surface.get_width()+50
    hauteur = texte_surface.get_height()+50
    message_surface = (largeur, hauteur)
    fond_surface = pg.Surface(message_surface)
    fond_surface.fill(COLORS['TRANSPARENT_BLACK'])
    fond_surface.blit(texte_surface, (0, 0))
    return fond_surface
#  Créer les objets de texte avec fond
abandon_message = creer_texte_avec_fond("Abandon!", police, COLORS['WHITE'], COLORS['GREY'])
fail_abandon_message = creer_texte_avec_fond("Abandon!", police, COLORS['WHITE'], COLORS['GREY'])
fail_attack_message = creer_texte_avec_fond("Attaque ratée!", police, COLORS['WHITE'], COLORS['GREY'])
# Positionner les textes à l'écran
abandon_message_rect = abandon_message.get_rect(center=(DSP_WIDTH // 2, DSP_HEIGHT // 2))
fail_abandon_message_rect = abandon_message.get_rect(center=(DSP_WIDTH // 2, DSP_HEIGHT // 2))
fail_attack_message_message_rect = fail_attack_message.get_rect(center=(DSP_WIDTH // 2, DSP_HEIGHT // 2))



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
        self.escape = False
        self.runner = True

    def draw_p1(self, k, screen=SCREEN):
        if len(self.__p1_sprites) == 2:
            screen.blit(pg.transform.scale(self.__p1_sprites[k], size=POK1_DIMS), (POK_1_x, POK_1_y))
        else:
            if k == 0:
                screen.blit(pg.transform.scale(self.__p1_sprites[0], size=POK1_DIMS), (POK_1_x, POK_1_y))

    def draw_p2(self, k, screen=SCREEN):
        if len (self.__p2_sprites) == 2:
            screen.blit(pg.transform.scale(self.__p2_sprites[k], size=POK2_DIMS), (POK_2_x, POK_2_y))
        else:
            if k == 0:
                screen.blit(pg.transform.scale(self.__p2_sprites[k], size=POK2_DIMS), (POK_2_x, POK_2_y))


    def draw_bar(self, screen=SCREEN):
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

    def atk1(self):
        if not self.dodge(self.p2) and self.get_hp()[0] > 0:
            self.attack1()
            for i in [1, 0] * 2:
                self.draw_p2(k=i)
                pg.display.flip()
                pg.time.delay(250)
            print('Attaque réussie!!!')
        else:
            print('Attaque ratée!!!')
        self.current = 2
        pg.time.delay(250)

    def atk1_spe(self):
        if not self.dodge(self.p2) and self.get_hp()[0] > 0:
            self.attack1(atk='spe')

            for i in [1, 0] * 2:
                self.draw_p2(k=i)
                pg.display.flip()
                pg.time.delay(250)
            print('Attaque réussie!!!')
        else:
            print('Attaque ratée!!!')
        self.current = 2
        pg.time.delay(250)
    
    def flee(self):
        chance_rate = log(1 + random()) * self.p1.speed ** (1 / 3)
        print(chance_rate)
        if chance_rate > 2:
            self.runner = False
            print('Flee activate')
            SCREEN.blit(abandon_message, abandon_message_rect)
            self.current = 0
            pg.display.flip()
            pg.time.delay(1000)

        else:
            SCREEN.blit(fail_abandon_message, abandon_message_rect)
            return False

    def change(self, id_pokemon=None):
        if id_pokemon is None:
            pokdex = GuiDex(save=POKEDEX_SAVE)
            id_pok = pokdex.display()
        else:
            pokdex = GuiDex(save=POKEDEX_SAVE)
            pokdex.add_pokemon(id_pok=id_pokemon)
            id_pok = id_pokemon
        if isinstance(id_pok, int):
            self.change_pok(pokdex.get_pokemon(id_pok))
            self.__p1_sprites = [pg.image.load(f"{SP_POK_PATH}{self.p1.id_pok}-regular.png")]
            if os.path.isfile(f'{SP_POK_PATH}{self.p1.id_pok}-shiny.png'):
                self.__p1_sprites.append(pg.image.load(f"{SP_POK_PATH}{self.p1.id_pok}-shiny.png"))


    def play(self):
        pg.init()
        map1 = Map()
        font_size = 15
        atk = Button(position=(550, 470), size=(100, 50), clr=(220, 220, 220), cngclr=(255, 0, 0),
                     func=self.atk1, text='Atk.')
        spe_atk = Button((700, 470), (100, 50), (220, 220, 220), (255, 0, 0),
                         func=self.atk1_spe, text='Spe. Atk.')
        flee = Button((550, 540), (100, 50), (220, 220, 220), (255, 0, 0),
                      func=self.flee, text='Flee')
        change = Button((700, 540), (100, 50), (220, 220, 220), (255, 0, 0),
                        func=self.change, text='Ch. Pok')
        button_list = [atk, spe_atk, flee, change]

        SCREEN.blit(map1.image, map1.rect)
        self.draw_bar()
        self.draw_p1(k=0)
        self.draw_p2(k=0)
        for b in button_list:
            b.draw(SCREEN)

        pg.display.flip()
        pg.time.delay(250)

        while self.runner:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    runner = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        runner = False
                    if self.current == 1:
                        if event.key == pg.K_a:
                            self.atk1()
                            self.draw_bar()
                            pg.display.flip()
                        if event.key == pg.K_s:
                            self.atk1_spe()
                            self.draw_bar()
                            pg.display.flip()
                        if event.key == pg.K_f:
                            if self.flee():
                                self.current = 0
                                self.escape = True
                                self.runner = False
                                print('Flee activate')
                                break
                        if event.key == pg.K_c:
                            self.change()
                            self.current = 2

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.current == 1:
                        pos = pg.mouse.get_pos()
                        for b in button_list:
                            if b.rect.collidepoint(pos):
                                b.call_back()
                                self.current = 2
                                self.draw_bar()
                                pg.display.flip()

            if self.current == 2:
                if self.get_hp()[1] != 0 and self.get_hp()[0] != 0:
                    if not self.dodge(self.p1) and self.get_hp()[1] > 0:
                        self.attack2(atk=choice(['atk', 'spe']))
                    for i in [1, 0] * 2:
                        self.draw_p1(k=i)
                        pg.display.flip()
                        pg.time.delay(250)
                    print('Attaque réussie!!!')
                    if self.search_ko():
                        self.current = 0
                else:
                    print('Attaque ratée')
                pg.time.delay(1)
                self.current = 1
                self.draw_bar()
                pg.display.flip()

            if self.search_ko():
                self.current = 0

            if self.current == 0:
                if self.p1.evolution:
                    self.dex.add_pokemon(self.p1.evolution[0]['pokedexId'])
                    self.dex.save_pokedex()
                    print(self.p1.evolution[0]['pokedexId'])
                    self.change(self.p1.evolution[0]['pokedexId'])


            SCREEN.blit(map1.image, map1.rect)
            self.draw_bar()
            self.draw_p1(k=0)
            self.draw_p2(k=0)
            if self.current == 1:
                for b in button_list:
                    b.draw(SCREEN)

            pg.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    dex = GuiDex()
    dexc = GuiDex(save=POKEDEX_FILE)
    print(dex.read_pokedex())
    print(dex.read_pokedex()[0]['pokedexId'])
    pok1, pok2 = Pokemon(dex.get_pokemon(dex.read_pokedex()[0]['pokedexId'])), Pokemon(dexc.get_pokemon(randint(1, 1017)))
    battle = GuiBattle(pok1, pok2, dex)
    battle.play()

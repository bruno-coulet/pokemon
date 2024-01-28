#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET, Cyril GENISSON
@file: gui_battle.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from math import log
from battle import Battle
from pokemon import Pokemon
from pokedex import Pokedex
from but import Button
from gui_dex import GuiDex
from map import Map
import pygame as pg
from random import random, randint, choice
import os


POK_1_HEIGHT = 300
POK_1_WIDTH = 300
POK1_DIMS = (300, 300)
POK2_DIMS = (250, 250)
POK_1_x = 50
POK_1_y = 200

POK_2_HEIGHT = 250
POK_2_WIDTH = 250
POK_2_x = 455
POK_2_y = 125

BTL_BTN_SIZE = (180, 50)
COLOR = COLORS['LIGHT_BLUE']
HOVER_COLOR = COLORS['HOVER_COLOR']

pg.font.init()
SCREEN_CENTER = (DSP_WIDTH//2, DSP_HEIGHT//2)
ACTION_MESSAGE_POLICE = pg.font.Font(KANIT, 30)
TURN_MESSAGE_POLICE = pg.font.Font(KANIT, 20)


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
        self.map1 = Map()
        self.escape = False
        self.runner = True
        self.no_flee = True

    def draw_pokemon_1(self, k, screen=SCREEN):
        ellipse_surface = pg.Surface((300, 800), pg.SRCALPHA)
        pg.draw.ellipse(ellipse_surface, COLORS['TRANSPARENT_CREME'], (0, 0, 300, 80))
        pg.draw.ellipse(ellipse_surface, COLORS['TRANSPARENT_GREEN'], (5, 5, 290, 70), width=5)
        pg.draw.ellipse(ellipse_surface, COLORS['TRANSPARENT_YELLOW'], (0, 0, 300, 80), width=5)
        screen.blit(ellipse_surface, (POK_1_x - 10, POK_1_y + 250))
        
        if len(self.__p1_sprites) == 2:
            screen.blit(pg.transform.scale(self.__p1_sprites[k], size=POK1_DIMS), (POK_1_x, POK_1_y))
        else:
            if k == 0:
                screen.blit(pg.transform.scale(self.__p1_sprites[0], size=POK1_DIMS), (POK_1_x, POK_1_y))

    def draw_pokemon_2(self, k, screen=SCREEN):
        ellipse_surface = pg.Surface((320, 120), pg.SRCALPHA)
        pg.draw.ellipse(ellipse_surface, COLORS['TRANSPARENT_CREME'], (0, 0, 300, 80))
        pg.draw.ellipse(ellipse_surface, COLORS['TRANSPARENT_RED'], (5, 5, 290, 70), width=5)
        pg.draw.ellipse(ellipse_surface, COLORS['TRANSPARENT_YELLOW'], (0, 0, 300, 80), width=5)
        screen.blit(ellipse_surface, (POK_2_x, POK_2_y + 200))

        if len(self.__p2_sprites) == 2:
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

    @staticmethod
    def message(text, color=COLORS['WHITE']):
        txt = ACTION_MESSAGE_POLICE.render(text, True, color)
        width = txt.get_width() + 40
        height = txt.get_height() + 40

        x = 20
        y = 20
        message_surface = pg.Surface((width, height), pg.SRCALPHA)
        message_surface.fill(COLORS['TRANSPARENT_BLACK'])
        message_surface.blit(txt, (x, y))
        return message_surface
    
    MESSAGES = {
        "abandon_message": message(text='Abandonner le combat!'),
        "esquive_message": message(text='Esquive'),
        "no_flee": message(text='Fuite échouée'),
        "failed_abandon_message": message(text='Echec de l\'abandon!'),
        "attack_message": message(text='Attaque!'),
        "failed_attack_message": message(text='Attaque ratée!'),
        "special_attack_message": message(text='Attaque spéciale !'),
        "failed_special_attack_message": message(text='Attaque spéciale ratée!'),
        "win_message": message(text='Victoire !'),
        "evolution": message(text='Evolution!!!'),
        "no_evolution": message(text='Evolution impossible'),
        "loose_message": message(text='Game over !'),
        "your_turn_message": message(text='A vous de jouer !'),
        "opponent_turn_message": message(text='Au tour de votre adversaire de jouer')
        }

    def call_message(self, message=None):
        if message in self.MESSAGES:
            SCREEN.blit(self.MESSAGES[message], self.MESSAGES[message].get_rect(center=SCREEN_CENTER))
            pg.display.flip()
            pg.time.delay(1500)
            self.refresh()

    def atk1(self):
        if not self.dodge(self.p2) and self.get_hp()[0] > 0:
            self.attack1()
            self.call_message("attack_message")
            for i in [1, 0] * 2:
                self.draw_pokemon_2(k=i)
                pg.display.flip()
                pg.time.delay(250)
            print('Attaque réussie!!!')

        else:
            self.call_message("failed_attack_message")
            print('Attaque ratée!!!')

        self.current = 2
        pg.time.delay(500)

    def atk1_spe(self):
        if not self.dodge(self.p2) and self.get_hp()[0] > 0:
            self.attack1(atk='spe')
            self.call_message("special_attack_message")
            for i in [1, 0] * 2:
                self.draw_pokemon_2(k=i)
                pg.display.flip()
                pg.time.delay(250)
        else:
            self.call_message("failed_special_attack_message")
        self.current = 2
        pg.time.delay(500)
    
    def flee(self):
        chance_rate = log(1 + random()) * self.p1.speed ** (1 / 3)
        print(chance_rate)
        if chance_rate > 2:
            self.runner = False
            self.current = 0
            self.no_flee = False
            self.call_message("abandon_message")
        else:
            self.call_message("no_flee")
            self.current = 2
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
        self.refresh()
        pg.time.delay(250)

    def refresh(self):
        SCREEN.blit(self.map1.image, self.map1.rect)
        self.draw_bar()
        self.draw_pokemon_1(k=0)
        self.draw_pokemon_2(k=0)
        pg.display.flip()

    def play(self):
        pg.init()
        button_area_width = 420
        button_area_height = 150
        button_area = pg.Surface((button_area_width, button_area_height), pg.SRCALPHA)
        button_area.fill(COLORS['TRANSPARENT_BLACK'])
        button_area_rect = button_area.get_rect(topleft=(370, 430))
        atk = Button(position=(480, 470), size=BTL_BTN_SIZE, func=self.atk1, text='Attaque')
        spe_atk = Button((680, 470), BTL_BTN_SIZE, func=self.atk1_spe, text='Attaque spéciale')
        flee = Button((480, 540), BTL_BTN_SIZE, func=self.flee, text='Abandon')
        change = Button((680, 540), BTL_BTN_SIZE, func=self.change, text='Changer de Pokemon')
        button_list = [atk, spe_atk, flee, change]

        SCREEN.blit(self.map1.image, self.map1.rect)
        SCREEN.blit(button_area, button_area_rect)
        self.draw_bar()
        self.draw_pokemon_1(k=0)
        self.draw_pokemon_2(k=0)
        for b in button_list:
            b.draw(SCREEN)
        pg.display.flip()
        pg.time.delay(1500)

        while self.runner:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runner = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.runner = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.current == 1:
                        pos = pg.mouse.get_pos()
                        for b in button_list:
                            if b.rect.collidepoint(pos):
                                b.call_back()
                                self.draw_bar()
                                pg.display.flip()

            if self.current == 2:
                if self.get_hp()[1] != 0 and self.get_hp()[0] != 0:
                    self.call_message("opponent_turn_message")
                    if not self.dodge(self.p1) and self.get_hp()[1] > 0:
                        self.attack2(atk=choice(['atk', 'spe']))
                        for i in [1, 0] * 2:
                            self.draw_pokemon_1(k=i)
                            pg.display.flip()
                            pg.time.delay(250)
                    else:
                        self.call_message("esquive_message")
                    print('Attaque réussie!!!')
                    self.refresh()
                    if self.search_ko():
                        self.current = 0
                        hp1, hp2 = self.get_hp()
                        if hp1 == 0:
                            self.call_message("loose_message")
                else:
                    self.call_message("win_message")
                    self.current = 0
                pg.time.delay(1000)
                self.current = 1
                self.draw_bar()
                pg.display.flip()

            if self.search_ko():
                self.current = 0
                self.runner = False

            if self.current == 0:
                if self.get_hp()[0] > 0 and self.no_flee:
                    if self.p1.evolution:
                        self.call_message("evolution")
                        self.dex.add_pokemon(self.p1.evolution[0]['pokedexId'])
                        self.dex.save_pokedex()
                        print(self.p1.evolution[0]['pokedexId'])
                        self.change(self.p1.evolution[0]['pokedexId'])
                        self.refresh()
                        pg.time.delay(3000)
                    else:
                        self.call_message("no_evolution")

            if self.current == 1:
                SCREEN.blit(button_area, button_area_rect)
                for b in button_list:
                    b.draw(SCREEN)
            pg.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    dex = GuiDex()
    dexc = GuiDex(save=POKEDEX_FILE)
    print(dex.read_pokedex())
    print(dex.read_pokedex()[0]['pokedexId'])
    pok1 = Pokemon(dex.get_pokemon(dex.read_pokedex()[0]['pokedexId']))
    pok2 = Pokemon(dexc.get_pokemon(randint(1, 1017)))
    battle = GuiBattle(pok1, pok2, dex)
    battle.play()

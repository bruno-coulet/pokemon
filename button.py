#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET
@file: button.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from gui_battle import *
from map import Map
import pygame as pg
import os
from random import randint


BATTLE_BTN_WIDTH = 200
BATTLE_BTN_HEIGHT = 50

ATTACK_BTN_X = 380
ATTACK_BTN_Y = 450

SPECIAL_BTN_X = 590
SPECIAL_BTN_Y = 450

DODGE_BTN_X = 380
DODGE_BTN_Y = 525

CHANGE_BTN_X = 590
CHANGE_BTN_Y = 525

KANIT = 'assets/fonts/kanit_medium.ttf'
KANIT_BOLD = 'assets/fonts/kanit_extraboldItalic.ttf'
MARHEY = 'assets/fonts/marhey.ttf'



class Button:

    def __init__(self, btn_text, x, y, width, height, attribute ):
        pg.font.init()
        # self.FONT = pg.font.Font(None, 25)
        # self.FONT = pg.font.SysFont('arial', 25)
        # self.FONT = pg.font.Font(KANIT, 20)
        self.FONT = pg.font.Font(MARHEY, 18)
        self.btn_text = btn_text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.attribute = attribute

    def draw(self, screen):
        pg.draw.rect(screen, COLORS['ORANGE'], (self.x-2, self.y-2, self.width, self.height), border_radius=20)
        pg.draw.rect(screen, COLORS['YELLOW'], (self.x, self.y, self.width+4, self.height+4), border_radius=20)
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=20)
        text_surface = self.FONT.render(self.btn_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

class BattleButton(Button):
    def __init__(self, color, btn_text, x, y, width, height, attribute):
        super().__init__(btn_text, x, y, width, height, attribute)
        self.color = color

if __name__ == "__main__":
    pg.init()
    dex = Pokedex()
    dex.add_pokemon(1)
    dex.add_pokemon(2)
    pok1 = Pokemon(dex.get_pokemon(1))
    pok2 = Pokemon(dex.get_pokemon(2))
    battle = GuiBattle(pok1, pok2, dex)
    map1 = Map()


    attack_btn = BattleButton(btn_text = "Attaque", color = COLORS['RED'], x = ATTACK_BTN_X, y = ATTACK_BTN_Y, width = BATTLE_BTN_WIDTH, height = BATTLE_BTN_HEIGHT, attribute = 'atk_method')
    special_btn = BattleButton(btn_text = "Attaque spéciale", color = COLORS['DARK_RED'], x = SPECIAL_BTN_X, y = SPECIAL_BTN_Y, width = BATTLE_BTN_WIDTH, height = BATTLE_BTN_HEIGHT, attribute = 'spe_atk')
    dodge_btn = BattleButton(btn_text = "Courage, fuyons !", color = COLORS['LIGHT_BLUE'], x = DODGE_BTN_X, y = DODGE_BTN_Y, width = BATTLE_BTN_WIDTH, height = BATTLE_BTN_HEIGHT, attribute = '___')
    change_btn = BattleButton(btn_text = "Changer de pokémon", color = COLORS['DARK_BLUE'], x = CHANGE_BTN_X, y = CHANGE_BTN_Y, width = BATTLE_BTN_WIDTH, height = BATTLE_BTN_HEIGHT, attribute = '___')

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        SCREEN.blit(map1.image, map1.rect)
        battle.draw_bar(SCREEN)
        battle.draw_p1(SCREEN, k=0)
        battle.draw_p2(SCREEN, k=0)
        attack_btn.draw(SCREEN)
        special_btn.draw(SCREEN)
        dodge_btn.draw(SCREEN)
        change_btn.draw(SCREEN)


        pg.display.flip()

    pg.quit()

        


    # ATTACK_BUTTON = pg.Rect(ATTACK_BTN_X,ATTACK_BTN_Y,BATTLE_BTN_WIDTH,BATTLE_BTN_HEIGHT)
    # SPECIAL_BUTTON = pg.Rect(SPECIAL_BTN_X,SPECIAL_BTN_Y,BATTLE_BTN_WIDTH,BATTLE_BTN_HEIGHT)
    # DODGE_BUTTON = pg.Rect(DODGE_BTN_X,DODGE_BTN_Y,BATTLE_BTN_WIDTH,BATTLE_BTN_HEIGHT)
    # CHANGE_BUTTON = pg.Rect(CHANGE_BTN_X,CHANGE_BTN_Y,BATTLE_BTN_WIDTH,BATTLE_BTN_HEIGHT)
    # def draw_btn(self):
    #     pg.draw.rect(SCREEN, 'RED', ATTACK_BUTTON)
    #     pg.draw.rect(SCREEN, 'RED', SPECIAL_BUTTON)
    #     pg.draw.rect(SCREEN, 'RED', DODGE_BUTTON)
    #     pg.draw.rect(SCREEN, 'RED', CHANGE_BUTTON)


        # Draw the button
        # button.draw_attack_btn(SCREEN)
        # button.draw_spe_attack_btn(SCREEN)
        # button.draw_dodge_btn(SCREEN)
        # button.draw_change_pok_btn(SCREEN)


        # Draw the special button
        # special_button.draw()
        


    # def draw_text(self, text, CREME, SCREEN, x, y):
    #     textobj = self.FONT.render(text, 1, COLORS['CREME'])
    #     textrect = textobj.get_rect()
    #     textrect.topleft = (0, 0)
    #     SCREEN.blit(textobj, textrect) 

    # def draw_attack_btn(self, screen):
    #     pg.draw.rect(screen, 'RED', (380, 450, BTN_WIDTH, BTN_HEIGHT),border_radius=20)
    #     """" Create a font object,
    #         Create a text surface
    #         Get the text rectangle
    #         Center the text on the button
    #         Blit the text onto the screen
    #     """
    #     font = pg.font.Font(None, 36)  
    #     text_surface = font.render("Attack", True, (255, 255, 255)) 
    #     text_rect = text_surface.get_rect()
    #     text_rect.center = (380+BTN_WIDTH // 2, 450+BTN_HEIGHT // 2)
    #     screen.blit(text_surface, text_rect)
        

    # def draw_spe_attack_btn(self, screen):
    #     pg.draw.rect(screen, 'CYAN', (SPECIAL_BTN_X, SPECIAL_BTN_Y, BTN_WIDTH, BTN_HEIGHT))
        
    # def draw_dodge_btn(self, screen):
    #     pg.draw.rect(screen, 'GREY', (380, 525, BTN_WIDTH, BTN_HEIGHT))

    # def draw_change_pok_btn(self, screen):
    #     pg.draw.rect(screen, 'GREY', (590, 525, BTN_WIDTH, BTN_HEIGHT))
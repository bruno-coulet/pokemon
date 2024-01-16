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


"""    A faire:
    - les boutons avec la gestion de la souris ou du clavier pour les différents choix:
    - attaque
    - attaque spéciale
    - fuite
    - changer de pokémon."""




BTN_WIDTH = 200
BTN_HEIGHT = 50

class Button:

    def __init__(self, screen, attack_btn, spe_attack_btn, dodge_btn, change_pok_btn):
        pg.font.init()
        self.FONT = pg.font.Font(None, 36)
        self.attack_btn = attack_btn
        self.spe_attack_btn = spe_attack_btn
        self.dodge_btn =  dodge_btn
        self.change_pok_btn = change_pok_btn

    def draw_text(self, text, CREME, SCREEN, x, y):
        textobj = self.FONT.render(text, 1, COLORS['CREME'])
        textrect = textobj.get_rect()
        textrect.topleft = (0, 0)
        SCREEN.blit(textobj, textrect) 

    def draw_attack_btn(self, screen):
        pg.draw.rect(screen, 'RED', (380, 450, BTN_WIDTH, BTN_HEIGHT),border_radius=20)
        # Create a font object
        font = pg.font.Font(None, 36)  
        # Create a text surface
        text_surface = font.render("Attack", True, (255, 255, 255)) 
        # Get the text rectangle
        text_rect = text_surface.get_rect()
        # Center the text on the button
        text_rect.center = (380+BTN_WIDTH // 2, 450+BTN_HEIGHT // 2)
        # Blit the text onto the screen
        screen.blit(text_surface, text_rect)

    def draw_spe_attack_btn(self, screen):
        pg.draw.rect(screen, 'CYAN', (SPECIAL_BTN_X, SPECIAL_BTN_Y, BTN_WIDTH, BTN_HEIGHT),border_radius=20)
        self.draw_text("attaque spéciale", self.FONT, COLORS['CREME'], SCREEN, (0, 0))
        # self.texte = "Attaque spéciale"
        text_surface = font.render("Attaque spéciale", True, (255, 255, 255)) 
        # Get the text rectangle
        text_rect = text_surface.get_rect()
        # Center the text on the button
        text_rect.center = (380+BTN_WIDTH // 2, 450+BTN_HEIGHT // 2)
        # Blit the text onto the screen
        screen.blit(text_surface, text_rect)

        
    def draw_dodge_btn(self, screen):
        pg.draw.rect(screen, 'GREY', (380, 525, BTN_WIDTH, BTN_HEIGHT),border_radius=20)

    def draw_change_pok_btn(self, screen):
        pg.draw.rect(screen, 'GREY', (590, 525, BTN_WIDTH, BTN_HEIGHT),border_radius=20)


    """
    TITLE = 'JEU DE MORPION'
    TITLE_FONT = pygame.font.Font(None, 80)
    FONT = pygame.font.Font(None, 50)

    def draw_text(text, FONT, CREME, SCREEN, x, y):
    textobj = FONT.render(text, 1, CREME)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    SCREEN.blit(textobj, textrect) 
    """


if __name__ == "__main__":
    pg.init()
    dex = Pokedex()
    dex.add_pokemon(1)
    dex.add_pokemon(2)
    pok1 = Pokemon(dex.get_pokemon(1))
    pok2 = Pokemon(dex.get_pokemon(2))
    battle = GuiBattle(pok1, pok2, dex)
    map1 = Map()
    button = Button(SCREEN, None, None, None, None)
    # SCREEN = pg.display.set_mode((DSP_WIDTH, DSP_HEIGHT))

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        SCREEN.blit(map1.image, map1.rect)
        battle.draw_bar(SCREEN)
        battle.draw_p1(SCREEN, k=0)
        battle.draw_p2(SCREEN, k=0)
        
        # Draw the button
        button.draw_attack_btn(SCREEN)
        button.draw_spe_attack_btn(SCREEN)
        # button.draw_dodge_btn(SCREEN)
        # button.draw_change_pok_btn(SCREEN)


        pg.display.flip()

    pg.quit()

        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON, Bruno COULET
@file: game.py

@project: Pokémon
@licence: GPLv3
"""

""" faire 5 boutons:
                      - Nouvelle partie
                      - Continuer
                      - Pokédex
                      - Générique
                      - Crédits     """

from constants import *
from map import Map
from but import Button, MenuButton


BTN_WIDTH = 200
BTN_HEIGHT = 50
BTN_SIZE = (BTN_WIDTH, BTN_HEIGHT)
BTN_COLOR = COLORS['LIGHT_BLUE']
BTN_HOVER_COLOR = COLORS['DARK_BLUE']
BTN_TXT_COLOR = COLORS['WHITE']

class Game:

    def __init__(self):
        self.runner = True
    
    def run(self):
        map1 = Map(image="assets/images/cerisier.jpg")
        SCREEN.blit(map1.image, map1.rect)

        pg.font.init()



        # Initialisation des boutons
        # class Button:
        # def __init__(self, position, size, clr=COLORS['GREY'], cngclr=None, func=None, text='', font="Segoe Print", font_size=16, font_clr=COLORS['BLACK']):
        new_game = MenuButton(position = (100, 100), size = BTN_SIZE, clr= BTN_COLOR, cngclr= BTN_HOVER_COLOR, func=None, text='Nouvelle partie', font_clr = BTN_TXT_COLOR )
        go_on = MenuButton(position = (100, 150), size = BTN_SIZE, clr= BTN_COLOR, cngclr= BTN_HOVER_COLOR,  func=None, text='Continuer', font_clr = BTN_TXT_COLOR)
        pokedex = MenuButton((100, 200), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR, text='Pokedex', font_clr = BTN_TXT_COLOR)
        generic = MenuButton((100, 250), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR, text='Générique', font_clr = BTN_TXT_COLOR)
        credit = MenuButton((100, 350), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR,  text='Crédits',font_clr = BTN_TXT_COLOR)

        pg.display.flip()


        while self.runner:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runner = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.runner = False

            # Affichage des boutons à l'intérieur de la boucle
            new_game.draw(SCREEN)
            go_on.draw(SCREEN)
            pokedex.draw(SCREEN)
            generic.draw(SCREEN)
            credit.draw(SCREEN)

            pg.display.flip() 
            
        clock.tick(FPS)

if __name__ == '__main__':

    game = Game()
    game.run()

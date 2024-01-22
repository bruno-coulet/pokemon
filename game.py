#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON, Bruno COULET
@file: game.py

@project: Pokémon
@licence: GPLv3
"""

""" J'ARRIVE PAS A CHANGER LA TYPO
    FAUT AJOUTER UN FOND NOIR TRANSPARENT ENTRE LE FOND ET LES PERSONNAGES
"""


from constants import *
from map import Map
from but import Button, MenuButton


BTN_WIDTH = 200
BTN_HEIGHT = 50
BTN_SIZE = (BTN_WIDTH, BTN_HEIGHT)
BTN_COLOR = COLORS['LIGHT_BLUE']
BTN_HOVER_COLOR = COLORS['ORANGE']
BTN_TXT_COLOR = COLORS['CREME']

hypocampe = pg.transform.scale(pg.image.load("assets/images/117-shiny.png"), (150, 150))
dinosaure = pg.transform.scale(pg.image.load("assets/images/112-regular.png"), (450, 450))
escargot = pg.transform.scale(pg.image.load("assets/images/138-regular.png"), (150, 150))
crabe = pg.transform.scale(pg.image.load("assets/images/347-regular.png"), (350, 350))
# -----------CI DESSOUS : PYGAME FLIP NE FLIP RIEN DU TOUT ----------------
homard = pg.transform.flip(pg.transform.scale(pg.image.load("assets/images/402-regular.png"), (150, 150)), True, False)


class Game:

    def __init__(self):
        self.runner = True
    
    def run(self):
        #  Affiche le fond
        map1 = Map(image="assets/images/cerisier.jpg")

        # Crée un gris_tranparent
        gris_tranparent = pg.Surface((DSP_WIDTH, DSP_HEIGHT), pg.SRCALPHA)
        gris_tranparent.fill((COLORS['TRANSPARENT_BLACK']))

        # Affiche le gris transparent
        SCREEN.blit(gris_tranparent, (0, 0))

        #  Affiche les personnages
        SCREEN.blit(map1.image, map1.rect)
        SCREEN.blit(hypocampe, (290,43))
        SCREEN.blit(dinosaure, (-10,160))
        SCREEN.blit(homard, (580,330))
        SCREEN.blit(escargot, (385,130))
        SCREEN.blit(crabe, (490,-30))
  
        # Initialise les polices
        pg.font.init()

        # Initialise les boutons
        new_game = MenuButton(position = (200, 100), size = BTN_SIZE, clr= BTN_COLOR, cngclr= BTN_HOVER_COLOR, func=None, text='Nouvelle partie', font_clr = BTN_TXT_COLOR, font = KANIT )
        go_on = MenuButton(position = (300, 200), size = BTN_SIZE, clr= BTN_COLOR, cngclr= BTN_HOVER_COLOR,  func=None, text='Continuer', font_clr = BTN_TXT_COLOR)
        pokedex = MenuButton((400, 300), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR, text='Pokedex', font_clr = BTN_TXT_COLOR)
        generic = MenuButton((500, 400), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR, text='Générique', font_clr = BTN_TXT_COLOR)
        credit = MenuButton((600, 500), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR,  text='Crédits',font_clr = BTN_TXT_COLOR)

        pg.display.flip()


        while self.runner:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runner = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.runner = False

            # Affiche le gris transparent CA MARCHE PAS? IL EST OPAQUE -----------------
            # SCREEN.blit(gris_tranparent, (0, 0))

            # Affichage les boutons
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

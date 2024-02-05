#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON, Bruno COULET
@file: game.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from map import Map
from but import MenuButton
from gui_battle import GuiBattle
from generic import Generic
from gui_dex import GuiDex
from pokemon import Pokemon
import random
import os




class Game:
    def __init__(self):
        self.runner = True
        self.load = False
    
    def loadpokedex(self):
        self.load = True
  
    def see_pokedex(self):
        if self.load:
            dex = GuiDex(save=POKEDEX_SAVE)
            dex.display()
        else:
            dex = GuiDex()
            dex.display()
            self.load = True

    def play(self):
        if self.load:
            if os.path.isfile(POKEDEX_SAVE):
                print("Loading Pokedex...")
                dex = GuiDex(save=POKEDEX_SAVE)
            else:
                print("Initializing Pokedex...")
                dex = GuiDex()
        else:
            print("Initializing Pokedex...")
            dex = GuiDex()
            self.load = True
        dexc = GuiDex(save=POKEDEX_FILE)
        pok1 = Pokemon(dex.get_pokemon(dex.read_pokedex()[0]['pokedexId']))
        pok2 = Pokemon(dexc.get_pokemon(random.randint(1, 1017)))
        battle = GuiBattle(pok1, pok2, dex)
        battle.play()

    @staticmethod
    def generic():
        g = Generic()
        g.play()

    def run(self):
        map1 = Map(image="assets/images/cerisier.jpg")
        hypocampe = pg.transform.scale(pg.image.load(f"{SP_POK_PATH}117-shiny.png"), (150, 150))
        dinosaure = pg.transform.scale(pg.image.load(f"{SP_POK_PATH}112-regular.png"), (450, 450))
        escargot = pg.transform.scale(pg.image.load(f"{SP_POK_PATH}138-regular.png"), (150, 150))
        crabe = pg.transform.scale(pg.image.load(f"{SP_POK_PATH}347-regular.png"), (350, 350))
        homard = pg.transform.flip(pg.transform.scale(pg.image.load(f"{SP_POK_PATH}402-regular.png"), (150, 150)), True,
                                   False)
        gris_tranparent = pg.Surface((DSP_WIDTH, DSP_HEIGHT), pg.SRCALPHA)                           
        gris_tranparent.fill((COLORS['TRANSPARENT_BLACK']))
        pg.font.init()
        new_game = MenuButton(position=(200, 100), size=BTN_SIZE, clr=BTN_COLOR, cngclr=BTN_HOVER_COLOR, func=self.play,
                              text='Nouveau combat', font_clr=BTN_TXT_COLOR)
        load = MenuButton(position=(300, 200), size=BTN_SIZE, clr=BTN_COLOR, cngclr=BTN_HOVER_COLOR,
                          func=self.loadpokedex, text='Charger une sauvegarde', font_clr=BTN_TXT_COLOR)
        pokedex = MenuButton((400, 300), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR, func=self.see_pokedex,
                             text='Pokedex', font_clr=BTN_TXT_COLOR)
        generic = MenuButton((500, 400), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR, func=self.generic, text='Générique',
                             font_clr=BTN_TXT_COLOR)
        credit = MenuButton((600, 500), BTN_SIZE, BTN_COLOR, BTN_HOVER_COLOR, text='Crédits',
                            font_clr=BTN_TXT_COLOR)

        button_list = [new_game, load, pokedex, generic, credit]
        pg.display.flip()

        while self.runner:
            SCREEN.blit(gris_tranparent, (0, 0))
            SCREEN.blit(map1.image, map1.rect)
            SCREEN.blit(hypocampe, (290, 43))
            SCREEN.blit(dinosaure, (-10, 160))
            SCREEN.blit(homard, (580, 330))
            SCREEN.blit(escargot, (385, 130))
            SCREEN.blit(crabe, (490, -30))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runner = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.runner = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()
                        for b in button_list:
                            if b.rect.collidepoint(pos):
                                b.call_back()
                                pg.display.flip()

            for b in button_list:
                b.draw(SCREEN)

            pg.display.flip() 

        clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

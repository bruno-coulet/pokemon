#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET, Cyril GENISSON
@file: gui_dex.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from pokedex import Pokedex
from map import Map
from but import Button

class GuiRec:
    def __init__(self, title, text, pos, dim):
        self.title = title
        self.text = text
        self.pos = pos
        self.dim = dim

class GuiDex(Pokedex):
    def __init__(self, save=None):
        super().__init__(save=save)
        self.current = 0
        self.__data = self.read_pokedex()
        self.len_data = len(self.read_pokedex())

    def minus_current(self):
        if self.current > 0:
            self.current -= 1
        else:
            self.current = self.len_data - 1
        print(self.update_view())

    def plus_current(self):
        if self.current < self.len_data - 1:
            self.current += 1

        else:
            self.current = 0
        print(self.update_view())

    def update_view(self):
        current_pokemon_id = self.__data[self.current]["pokedexId"]
        current_pokemon_name = self.__data[self.current]['name']['fr']
        current_pokemon_types = [type_data['name'] for type_data in self.__data[self.current]['types']]
        current_pokemon_sprite = f'{SP_POK_PATH}{current_pokemon_id}-regular.png'
        current_pokemon_stats_keys = [stat_data[0:] for stat_data in self.__data[self.current]['stats']]
        current_pokemon_stats_values = [self.__data[self.current]['stats'][stat] for stat in
                                        ['hp', 'atk', 'def', 'spe_atk', 'spe_def', 'vit']]
        return current_pokemon_id, current_pokemon_name, current_pokemon_types, current_pokemon_sprite, current_pokemon_stats_keys, current_pokemon_stats_values

    def display(self):
        pg.init()
        map = Map()
        font_size = 15
        font = pg.font.Font(None, font_size)
        SCREEN.blit(map.image, map.rect)

        prev_button = Button(position=(80, 100), size=(100, 50), clr=(220, 220, 220), cngclr=(255, 0, 0),
                             func=self.minus_current, text='')
        next_button = Button((220, 100), (100, 50), (220, 220, 220), (255, 0, 0), func=self.plus_current, text='')
        #select_button = Button((220, 100), (100))
        #save_button = Button((220, 100), ())
        #quit_button = Button((220))
        #button_list = [prev_button, next_button, select_button, save_button, quit_button]
        button_list = [prev_button, next_button]
        runner = True
        while runner:
            SCREEN.blit(map.image, map.rect)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    runner = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        runner = False

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()
                        for b in button_list:
                            if b.rect.collidepoint(pos):
                                b.call_back()

            for b in button_list:
                b.draw(SCREEN)

            pg.display.flip()
            clock.tick(FPS)
    pass


if __name__ == '__main__':
    dex = GuiDex()
    dex.display()

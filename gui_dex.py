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
        self.x, self.y = pos
        self.pos = pos
        self.dim = dim
        self.width, self.height = dim

    #  Grand Rectangles gris
    def draw_area(self, screen=SCREEN):
        description_background = pg.Surface(self.dim, pg.SRCALPHA)
        pg.draw.rect(description_background, COLORS['TRANSPARENT_BLACK'], (0, 0, self.width, self.height),
                     border_radius=20)
        screen.blit(description_background, (self.x, self.y))

    def draw_title(self, pok_name, screen=SCREEN):
        font = pg.font.Font(MARHEY, 25)
        #  crée un titre de description
        area_title = font.render(pok_name, True, (COLORS['WHITE']))
        text_rect = area_title.get_rect(center=(self.x + self.width // 2, self.y + 20))
        # affiche le titre de description
        screen.blit(area_title, text_rect)

    def draw_icon(self, pok_type=None, screen=SCREEN):
        icons = pok_type
        icon_size = 60
        spacing = 30
        for i, icon in enumerate(icons):
            icon_path = f"{SP_TYP_PATH}{icon}.png"
            try:
                icon_surface = pg.image.load(icon_path).convert_alpha()
                icon_x = self.x + self.width // 2 - 70 + i * (icon_size + spacing)
                screen.blit(icon_surface, (icon_x, self.y + 50))
            except FileNotFoundError:
                print(f"File not found: {icon_path}")

    def draw_description_area(self, screen=SCREEN):
        description_background = pg.Surface((self.width, self.height), pg.SRCALPHA)
        pg.draw.rect(description_background, COLORS['TRANSPARENT_BLACK'], (10, 120, self.width - 20, self.height - 130),
                     border_radius=20)
        screen.blit(description_background, (self.x, self.y))

    def draw_description_data(self, stats, screen=SCREEN):
        font = pg.font.Font(KANIT, 18)
        description_texts = [
            f"Points de vie: {stats[0]}",
            f"Attaque: {stats[1]}",
            f"Défense: {stats[2]}",
            f"Attaque Spéciale: {stats[3]}",
            f"Défense Spéciale: {stats[4]}",
            f"Vitesse: {stats[5]}"
        ]

        for i, description_text in enumerate(description_texts):
            text_surface = font.render(description_text, True, (COLORS['WHITE']))
            text_rect = text_surface.get_rect(topleft=(self.x + 20, self.y + 150 + i * 30))
            screen.blit(text_surface, text_rect)

    @staticmethod
    def draw_sprite(id_sprite=None, screen=SCREEN):

        sprite_path = f"assets/datas/sprites/Pokemons/{id_sprite}-regular.png"
        sprite_surface = pg.image.load(sprite_path).convert_alpha()
        resized_sprite = pg.transform.scale(sprite_surface, (300, 300))
        screen.blit(resized_sprite, (80, 100))


class GuiDex(Pokedex):
    def __init__(self, save=None):
        """Initialise 

        Args: fichier json, optional
        
        Récupère les infos du pokemon pour affichage    
        """
        super().__init__(save=save)
        self.current = 0
        self.__data = self.read_pokedex()
        print(self.__data)
        self.len_data = len(self.read_pokedex())
        self.current_pokemon_id = self.__data[self.current]["pokedexId"]
        self.current_pokemon_name = self.__data[self.current]['name']['fr']
        self.current_pokemon_types = [type_data['name'] for type_data in self.__data[self.current]['types']]
        self.current_pokemon_sprite = f'{SP_POK_PATH}{self.current_pokemon_id}-regular.png'
        self.current_pokemon_stats_keys = [stat_data[0:] for stat_data in self.__data[self.current]['stats']]
        self.current_pokemon_stats_values = [self.__data[self.current]['stats'][stat] for stat in
                                             ['hp', 'atk', 'def', 'spe_atk', 'spe_def', 'vit']]
        self.runner = True

    def minus_current(self):
        """Alterne le joueur"""
        if self.current > 0:
            self.current -= 1
            self.update()
        else:
            self.current = self.len_data - 1
            self.update()

    def plus_current(self):
        """Alterne le joueur"""
        if self.current < self.len_data - 1:
            self.current += 1
            self.update()

        else:
            self.current = 0
            self.update()

    def update(self):
        """Met à jour les infos du pokemon pour affichage"""
        self.len_data = len(self.read_pokedex())
        self.current_pokemon_id = self.__data[self.current]["pokedexId"]
        self.current_pokemon_name = self.__data[self.current]['name']['fr']
        self.current_pokemon_types = [type_data['name'] for type_data in self.__data[self.current]['types']]
        self.current_pokemon_sprite = f'{SP_POK_PATH}{self.current_pokemon_id}-regular.png'
        self.current_pokemon_stats_keys = [stat_data[0:] for stat_data in self.__data[self.current]['stats']]
        self.current_pokemon_stats_values = [self.__data[self.current]['stats'][stat] for stat in
                                             ['hp', 'atk', 'def', 'spe_atk', 'spe_def', 'vit']]

    def select(self):
        self.runner = False

    def quit(self):
        self.runner = False

    def display(self):
        """Initialise pygame, instancie la carte, crée et instancie les boutons, boucle de pokedex
        Returns: id du pokemon du joueur (int)
        """
        pg.init()
        map1 = Map()

        choose_pokemon = GuiRec(self.current_pokemon_name, None, (30, 60), (512 * 3 / 4, 512 * 3 / 4))
        pokemon_description = GuiRec("Caractéristiques", "None", ((DSP_WIDTH - 350 - 30), 60), (350, 512 * 3 / 4))

        prev_button = Button(position=(150, 520), size=(BTN_WIDTH/2, BTN_HEIGHT), clr=(BTN_COLOR), cngclr=(BTN_HOVER_COLOR),
                             func=self.minus_current, text='Prev.')
        next_button = Button((280, 520), (BTN_WIDTH/2, BTN_HEIGHT), (BTN_COLOR), (BTN_HOVER_COLOR), func=self.plus_current, text='Next')
        select_button = Button(position=(510, 520), size=(BTN_WIDTH/2, BTN_HEIGHT), clr=(BTN_COLOR), cngclr=(BTN_HOVER_COLOR),
                               func=self.select, text='Select')
        quit_button = Button((700, 520), (BTN_WIDTH/2, BTN_HEIGHT), (BTN_COLOR), (BTN_HOVER_COLOR), func=self.quit, text='Quit')
        button_list = [prev_button, next_button, select_button, select_button, quit_button]

        while self.runner:
            SCREEN.blit(map1.image, map1.rect)
            choose_pokemon.draw_area()
            choose_pokemon.draw_title(self.current_pokemon_name)
            choose_pokemon.draw_sprite(self.current_pokemon_id)
            pokemon_description.draw_area()
            pokemon_description.draw_title('Types')
            pokemon_description.draw_icon(self.current_pokemon_types)
            pokemon_description.draw_description_area()
            pokemon_description.draw_description_data(self.current_pokemon_stats_values)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runner = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.runner = False
                    if event.key == pg.K_LEFT:
                        self.minus_current()
                    if event.key == pg.K_RIGHT:
                        self.plus_current()
                    if event.key == pg.K_s:
                        self.select()
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
        return self.current_pokemon_id


if __name__ == '__main__':
    dex = GuiDex()
    dex.display()

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
        #                        Initialise une surface qui gère la transparence
        description_background = pg.Surface(self.dim, pg.SRCALPHA)
        #                        Applique la surface avec une couleur à un rectangle
        pg.draw.rect(description_background, COLORS['TRANSPARENT_BLACK'], (0, 0, self.width, self.height),
                     border_radius=20)
        # affiche la surface
        screen.blit(description_background, (self.x, self.y))

    # titre de la zone
    def draw_title(self, pok_name, screen=SCREEN):
        font = pg.font.Font(MARHEY, 25)
        #  crée un titre de description
        area_title = font.render(pok_name, True, (COLORS['WHITE']))
        text_rect = area_title.get_rect(center=(self.x + self.width // 2, self.y + 20))
        # affiche le titre de description
        screen.blit(area_title, text_rect)

    def draw_icon(self, pok_type=None, screen=SCREEN):
        # Charger l'icône et crée la surface
        icons = pok_type
        icon_size = 60
        spacing = 30  # Adjust the spacing as needed
        for i, icon in enumerate(icons):
            icon_path = f"{SP_TYP_PATH}{icon}.png"
            try:
                icon_surface = pg.image.load(icon_path).convert_alpha()
                # Afficher l'icône
                icon_x = self.x + self.width // 2 - 70 + i * (icon_size + spacing)
                screen.blit(icon_surface, (icon_x, self.y + 50))
            except FileNotFoundError:
                print(f"File not found: {icon_path}")

    # Rectangle gris plus petit
    def draw_description_area(self, screen=SCREEN):
        # Encore une zone gris transparent en fond
        description_background = pg.Surface((self.width, self.height), pg.SRCALPHA)
        pg.draw.rect(description_background, COLORS['TRANSPARENT_BLACK'], (10, 120, self.width - 20, self.height - 130),
                     border_radius=20)
        screen.blit(description_background, (self.x, self.y))

    def draw_description_data(self, stats, screen=SCREEN):
        font = pg.font.Font(KANIT, 18)
        #  crée le texte de description
        # # La méthode render prend le texte, un booléen pour l'antialiasing, et la couleur du texte en RGB.
        # description_text = self.FONT.render(self.text, True, (COLORS['WHITE']))
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
        # Charger l'image et crée la surface
        # sprite_path = f"assets/datas/sprites/Pokemons/1-regular.png"
        sprite_path = f"assets/datas/sprites/Pokemons/{id_sprite}-regular.png"
        sprite_surface = pg.image.load(sprite_path).convert_alpha()
        # Redimensionne l'image à la taille souhaitée
        resized_sprite = pg.transform.scale(sprite_surface, (300, 300))
        # Affiche l'image sur l'écran
        screen.blit(resized_sprite, (80, 100))


class GuiDex(Pokedex):
    def __init__(self, save=None):
        super().__init__(save=save)
        self.current = 0
        self.__data = self.read_pokedex()
        self.len_data = len(self.read_pokedex())
        self.current_pokemon_id = self.__data[self.current]["pokedexId"]
        self.current_pokemon_name = self.__data[self.current]['name']['fr']
        self.current_pokemon_types = [type_data['name'] for type_data in self.__data[self.current]['types']]
        self.current_pokemon_sprite = f'{SP_POK_PATH}{self.current_pokemon_id}-regular.png'
        self.current_pokemon_stats_keys = [stat_data[0:] for stat_data in self.__data[self.current]['stats']]
        self.current_pokemon_stats_values = [self.__data[self.current]['stats'][stat] for stat in
                                             ['hp', 'atk', 'def', 'spe_atk', 'spe_def', 'vit']]

    def minus_current(self):
        if self.current > 0:
            self.current -= 1
        else:
            self.current = self.len_data - 1

    def plus_current(self):
        if self.current < self.len_data - 1:
            self.current += 1

        else:
            self.current = 0

    def display(self):
        pg.init()
        map1 = Map()
        font_size = 15
        # font = pg.font.Font(None, font_size)
        SCREEN.blit(map1.image, map1.rect)

        choose_pokemon = GuiRec(self.current_pokemon_name, None, (30, 60), (512 * 3 / 4, 512 * 3 / 4))
        pokemon_description = GuiRec("Caractéristiques", "None", ((DSP_WIDTH - 350 - 30), 60), (350, 512 * 3 / 4))

        prev_button = Button(position=(150, 470), size=(100, 50), clr=(220, 220, 220), cngclr=(255, 0, 0),
                             func=self.minus_current, text='Prev.')
        next_button = Button((280, 470), (100, 50), (220, 220, 220), (255, 0, 0), func=self.plus_current, text='Next')
        # select_button = Button((220, 100), (100))
        # save_button = Button((220, 100), ())
        # quit_button = Button((220))
        # button_list = [prev_button, next_button, select_button, save_button, quit_button]
        button_list = [prev_button, next_button]
        # button_list = []
        runner = True
        while runner:
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
                    runner = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        runner = False
                    if event.key == pg.K_LEFT:
                        self.minus_current()
                    if event.key == pg.K_RIGHT:
                        self.plus_current()

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

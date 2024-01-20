#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET
@file: gui_pokedex.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
from gui_battle import *
from button import *
from map import Map
import os
from random import randint
from pokedex import Pokedex

TRANSPARENT_BLACK = (0,0,0,200)
HOVER_COLOR = (100, 200, 100)
COLORS['YELLOW'] = COLORS['YELLOW']

pg.font.init()
FONT_1 = pg.font.Font(MARHEY, 25)
FONT_2 =  pg.font.Font(KANIT, 18)

MENU_BTN_WIDTH = 120
MENU_BTN_HEIGHT = 50

PREV_BTN_X = 120
PREV_BTN_Y = 480

NEXT_BTN_X = 260
NEXT_BTN_Y = 480

VALID_BTN_X = 460
VALID_BTN_Y = 480

BACK_BTN_X = 630
BACK_BTN_Y = 480

""" IL FAUT Créer une variable current_pokemon pour pouvoir les afficher un à un.
    probablement ajouter cette variable aux paramètre de la classe GuiPokedex

dex.add_pokemon(current_pokemon)
pok1 = Pokemon(dex.get_pokemon(current_pokemon))

"""
current_pokemon = 1

class GuiPokedex(Pokedex):

    def __init__(self, title, text, x, y, width, height ):
        self.title = title
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    #  Grand Rectangles gris
    def draw_area(self, screen):
        #                        Initialise une surface qui gère la transparence
        description_background = pg.Surface((self.width, self.height), pg.SRCALPHA)
        #                        Applique la surface avec une couleur à un rectangle
        pg.draw.rect(description_background, TRANSPARENT_BLACK, (0, 0, self.width, self.height), border_radius=20)
        # affiche la surface
        screen.blit(description_background, (self.x, self.y))
    # titre de la zone
    def draw_title(self, screen):
        #  crée un titre de description
        area_title = FONT_1.render(self.title, True, (COLORS['WHITE']))
        text_rect = area_title.get_rect(center=(self.x + self.width // 2, self.y+20))
        # affiche le titre de description
        screen.blit(area_title, text_rect)
    
    def draw_icon(self, screen): 
    # Charger l'icône et crée la surface
        icons = current_pokemon_types
        icon_size = 60
        spacing = 30  # Adjust the spacing as needed
        for i, icon in enumerate(icons):
            icon_path = f"assets/datas/sprites/Types/{icon}.png"
            try:
                icon_surface = pg.image.load(icon_path).convert_alpha()
                # Afficher l'icône
                icon_x = self.x + self.width // 2 - 70 + i * (icon_size + spacing)
                screen.blit(icon_surface, (icon_x, self.y + 50))
            except FileNotFoundError:
                print(f"File not found: {icon_path}")

    # Rectangle gris plus petit
    def draw_description_area(self, screen):
        # Encore une zone gris transparent en fond
        description_background = pg.Surface((self.width, self.height), pg.SRCALPHA)
        pg.draw.rect(description_background, TRANSPARENT_BLACK, (10, 120, self.width-20, self.height-130), border_radius=20)
        screen.blit(description_background, (self.x, self.y))

    def draw_description_data(self, screen):
        #  crée le texte de description
        # # La méthode render prend le texte, un booléen pour l'antialiasing, et la couleur du texte en RGB.
        # description_text = self.FONT.render(self.text, True, (COLORS['WHITE']))
        description_texts = [
                    f"Points de vie: {current_pokemon_stats_values[0]}",
                    f"Attaque: {current_pokemon_stats_values[1]}",
                    f"Défense: {current_pokemon_stats_values[2]}",
                    f"Attaque Spéciale: {current_pokemon_stats_values[3]}",
                    f"Défense Spéciale: {current_pokemon_stats_values[4]}",
                    f"Vitesse: {current_pokemon_stats_values[5]}"
                             ]

        for i, description_text in enumerate(description_texts):
            text_surface = FONT_2.render(description_text, True, (COLORS['WHITE']))
            text_rect = text_surface.get_rect(topleft=(self.x + 20, self.y + 150 + i * 30))
            screen.blit(text_surface, text_rect)
            
    def draw_sprite(self, screen):
        # Charger l'image et crée la surface
        # sprite_path = f"assets/datas/sprites/Pokemons/1-regular.png"
        sprite_path = f"assets/datas/sprites/Pokemons/{current_pokemon_id}-regular.png"
        sprite_surface = pg.image.load(sprite_path).convert_alpha()
        # Redimensionne l'image à la taille souhaitée
        resized_sprite = pg.transform.scale(sprite_surface, (300, 300))
        # Affiche l'image sur l'écran
        screen.blit(resized_sprite, (80,100))
      
class MenuButton(Button):
    def __init__(self, color, btn_text, x, y, width, height, pok_type):
        super().__init__(btn_text, x, y, width, height, pok_type)
        self.color = color
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, screen):
        mx, my = pg.mouse.get_pos()

        if self.rect.collidepoint(mx, my):  # Use the collidepoint method on the instance
            pg.draw.rect(screen, HOVER_COLOR, self, border_radius=10)
        else:
            pg.draw.rect(screen, self.color, self, border_radius=10)

        # Réaffiche le texte des boutons qui avait disparu
        text = FONT_1.render(self.btn_text, True, COLORS['WHITE'])  # Assuming COLORS is defined somewhere
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
    
class NavButton(Button):
    def __init__(self, color, btn_text, x, y, width, height, pok_type):
        super().__init__(btn_text, x, y, width, height, pok_type)
        self.color = color
        self.points = [(x, y+25), (x + 50, y), (x + 50, y + 50) ]
        self.hover_points = [(x-4, y+25), (x + 54, y-4), (x + 54, y + 54) ]
        self.hover_2_points = [(x-8, y+25), (x + 56, y-8), (x + 56, y + 58) ]
        self.rect = pg.Rect(x, y, width, height)
        self.image = None  # TENTATIVE DE FLIP - CREE L'ATTRIBUT IMAGE

    def draw(self, screen):
        mx, my = pg.mouse.get_pos()

        # TENTATIVE DE FLIP - CREE UNE SURFACE
        # self.image = pg.Surface((self.rect.width, self.rect.height), pg.SRCALPHA)

        # Hover = True -> dessine 2 triangles (fond jaune et vert) puis le triangle couleur hover.
        if self.rect.collidepoint(mx, my):
            pg.draw.polygon(screen, COLORS['YELLOW'],self.hover_2_points)
            pg.draw.polygon(screen, HOVER_COLOR,self.hover_points)
            pg.draw.polygon(screen, self.color, self.points)
        # Hover = False -> dessine juste le triangle couleur originale
        else:
            pg.draw.polygon(screen, self.color, self.points)

        # # TENTATIVE DE FLIP - SI L'ATTRIBUT IMAGE EXISTE ON LE FLIP
        # if self.image is not None:
        #     next_btn_flipped = pg.transform.flip(self.image, True, False)
        #     screen.blit(next_btn_flipped, self.rect.topleft)
        # else:
        #     screen.blit(self.image, self.rect.topleft)

        # AFFICHE LE TEXTE DES BOUTONS - ON N'AFFICHE PLUS LE TEXTE
        # text = FONT_1.render(self.btn_text, True, COLORS['WHITE'])
        # text_rect = text.get_rect(center=self.rect.center)
        # screen.blit(text, text_rect)

if __name__ == "__main__":
    pg.init()

    # ajoute un pokemon
    pokedex = Pokedex()
    pokedex.add_pokemon(current_pokemon)
    # Read the pokedex data
    pok_data = pokedex.read_pokedex()
    # UN SEUL POKEMON, DONC UN SEUL ELEMENT DANS LA LISTE pok_data, L'INDEX [0]
    current_pokemon_id = pok_data[0]["pokedexId"]
    current_pokemon_name = pok_data[0]['name']['fr']
    current_pokemon_types = [type_data['name'] for type_data in pok_data[0]['types']]
    current_pokemon_sprite = pok_data[0]['sprites']['regular']
    current_pokemon_stats_keys = [stat_data[0:] for stat_data in pok_data[0]['stats']]
    current_pokemon_stats_values = [pok_data[0]['stats'][stat] for stat in ['hp', 'atk', 'def', 'spe_atk', 'spe_def', 'vit']]

    # Instancie le fond
    menu_background = Map()
    # Instancie le portrait et la description du pokemon
    choose_pokemon = GuiPokedex(current_pokemon_name, None, 30, 60, 512*3/4, 512*3/4)
    pokemon_description = GuiPokedex("Caractéristiques", f"hp: {current_pokemon_stats_values[1]}\nhp: {current_pokemon_stats_values[1]}",(DSP_WIDTH - 350 - 30), 60, 350, 512*3/4)
    # pokemon_description = GuiPokedex(f"hp: {current_pokemon_stats_values[1]}", str(current_pokemon_stats_values[4]), (DSP_WIDTH - 350 - 30), 60, 350, 512*3/4)
    
    # Instancie les boutons
    previous_btn = NavButton(btn_text = "Précedent", color = COLORS['RED'], x = PREV_BTN_X, y = PREV_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = 'atk_method')
    next_btn = NavButton(btn_text = "Suivant", color = COLORS['DARK_RED'], x = NEXT_BTN_X, y = NEXT_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = 'spe_atk')
    select_btn = MenuButton(btn_text = "Valider", color = COLORS['LIGHT_BLUE'], x = VALID_BTN_X, y = VALID_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = '___')
    back_btn = MenuButton(btn_text = "Retour", color = COLORS['DARK_BLUE'], x = BACK_BTN_X, y = BACK_BTN_Y, width = MENU_BTN_WIDTH, height = MENU_BTN_HEIGHT, pok_type = '___')

    run = True
    while run:
    
        mx, my = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # clic
                pos = event.pos

        # Affiche le fond
        SCREEN.blit(menu_background.image, menu_background.rect)
        # Appel les méthodes de la zone portrait du pokemon A GAUCHE
        choose_pokemon.draw_area(SCREEN)
        choose_pokemon.draw_title(SCREEN)
        choose_pokemon.draw_sprite(SCREEN)
        # Appel les méthodes de la zone description du pokemon A DROITE
        pokemon_description.draw_area(SCREEN)
        pokemon_description.draw_title(SCREEN)
        pokemon_description.draw_icon(SCREEN)
        pokemon_description.draw_description_area(SCREEN)
        pokemon_description.draw_description_data(SCREEN)
        # Appel les méthodes des boutons EN BAS
        previous_btn.draw(SCREEN)
        next_btn.draw(SCREEN)       
        select_btn.draw(SCREEN)
        back_btn.draw(SCREEN)
        # ...

        pg.display.flip()

    pg.quit()
from constants import *
from menu import *
from pokedex import *
from pokemon import *
from battle import *
from map import Map
from gui_battle import * 
import random
import pygame as pg


# Initialize Pygame
pg.init()
run = True

# Intancie le pokedex
pokedex = Pokedex()
# Intancie le pokemon du joueur, l'ajoute au pokedex
pokedex.add_pokemon(1)
pok1 = Pokemon(pokedex.get_pokemon(1))

# Intancie le pokemon adversaire, l'ajoute au pokedex
pokedex.add_pokemon(2)
pok2 = Pokemon(pokedex.get_pokemon(2))

if __name__ == '__main__':

    map_instance = Map()
    gui_battle_instance = Gui_battle()


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    
        # Dessine la map sur l'écran
        SCREEN.blit(map_instance.image, map_instance.rect)

        # Dessine les sprites des Pokémons
        gui_battle_instance.draw_pokemon_1_sprite(SCREEN)
        gui_battle_instance.draw_pokemon_2_sprite(SCREEN)

        # Dessine les fonds de barre de vie
        gui_battle_instance.draw_pokemon_1_bar(SCREEN)
        gui_battle_instance.draw_pokemon_2_bar(SCREEN)
        # Dessine les de barres de vie
        gui_battle_instance.draw_pokemon_1_life(SCREEN)
        gui_battle_instance.draw_pokemon_2_life(SCREEN)

        # Dessine les dégats
        # gui_battle_instance.draw_pokemon_1_damage(SCREEN)
        # gui_battle_instance.draw_pokemon_2_damage(SCREEN)




        # Rafraîchir l'affichage
        pg.display.flip()
 

        




























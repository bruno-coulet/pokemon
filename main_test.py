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
# Intancie le pokemon du joueur, le 1er du pokedex et l'ajoute au pokedex
pokedex.add_pokemon(1)
pok1 = Pokemon(pokedex.get_pokemon(1))

if __name__ == '__main__':

    # Position initiale
    x, y = 50, 50
    # Création de l'instance de la classe Map
    map_instance = Map()
    # Création de l'instance de la classe GuiBattle
    gui_battle_instance = Gui_battle()

    # Boucle principale
    while True:
    # Gestion des événements
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    
        # Dessiner la map sur l'écran
        SCREEN.blit(map_instance.image, map_instance.rect)

        # Dessiner le sprite du Pokémon
        # pg.draw.rect(SCREEN, (self.pokemon1_sprite), (x, y, 50, 50))
        gui_battle_instance.draw_pokemon_sprite(SCREEN, x, y)

        # Rafraîchir l'affichage
        pg.display.flip()
 

        




























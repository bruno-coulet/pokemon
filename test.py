from constants import *
from pokedex import *
from pokemon import *
from battle import *
from map import Map
import pygame as pg


# Intancie le pokemon du joueur, le 1er du pokedex
pok1 = Pokemon(pokedex.get_pokemon(1))

if __name__ == '__main__':
    # Boucle principale
    while True:
    # Gestion des événements
        for event in pygame.event.get():
            if event.type == pg.QUIT:
                pg.quit()

from constants import *
from battle import *
from map import Map
import pygame as pg

"""La class Gui_battle doit avoir toutes les méthodes pour gérer l'affichage des différents éléments:
    - les 2 sprite des 2 pokémons
    - leur barre hp progressant au cours des attaques,
    - les boutons avec la gestion de la souris ou du clavier pour les différents choix:
    - attaque
    - attaque spéciale
    - fuite
    - changer de pokémon.
    
    Enfin il faudra une méthode spéciale pour afficher un  texte de quelques mots au milieu ou alors dans un encart de l'écran pour suivre les différentes actions.
"""
        # Intancie le pokemon du joueur, le 1er du pokedex
        # pok1 = Pokemon(pokedex.get_pokemon(1))

class Gui_battle:
    def __init__(self):
        pg.init()        


        # Charger les sprites des deux Pokémon
        self.pokemon1_sprite = pg.image.load("path_to_pokemon1_sprite.png" "pokedex/....")#json_data[id_pok]['sprites']['regular']
        self.pokemon2_sprite = pg.image.load("path_to_pokemon2_sprite.png")

        # Charger les sprites des barres de HP
        self.hp_bar_sprite = pg.image.load("path_to_hp_bar_sprite.png")

        # Définir la position initiale des éléments
        self.pokemon1_position = (100, 400)
        self.pokemon2_position = (550, 100)
        self.hp_bar_position = (100, 50)


    def display_pokemon_sprites(self):
        # Afficher les sprites des deux Pokémon
        self.screen.blit(self.pokemon1_sprite, self.pokemon1_position)
        self.screen.blit(self.pokemon2_sprite, self.pokemon2_position)

    def display_hp_bars(self, hp_percentage_pokemon1, hp_percentage_pokemon2):
        # Afficher les barres de HP en fonction du pourcentage de HP restant
        self.screen.blit(self.hp_bar_sprite, self.hp_bar_position)

        # Dessiner la barre de HP pour le Pokémon 1
        pg.draw.rect(self.screen, (0, 255, 0), (self.hp_bar_position[0] + 10, self.hp_bar_position[1] + 10,
                                                hp_percentage_pokemon1 * 2, 10))

        # Dessiner la barre de HP pour le Pokémon 2
        pg.draw.rect(self.screen, (0, 255, 0), (self.hp_bar_position[0] + 400, self.hp_bar_position[1] + 10,
                                                hp_percentage_pokemon2 * 2, 10))

    def display_text(self, text):
        # Afficher du texte au milieu de l'écran
        font = pg.font.Font(None, 36)
        text_render = font.render(text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=(400, 300))
        self.screen.blit(text_render, text_rect)

    def update_display(self):
        # Mise à jour de l'affichage
        pg.display.flip()

    def handle_events(self):
        # Gérer les événements (clavier, souris, etc.)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.choice = "Attaque"
                elif event.key == pg.K_s:
                    self.choice = "Attaque spéciale"
                elif event.key == pg.K_f:
                    self.choice = "Fuite"
                elif event.key == pg.K_c:
                    self.choice = "Changer de Pokémon"

    def run_battle(self):
        clock = pg.time.Clock()

        while True:
            self.handle_events()

            # Exemple de pourcentage de HP restant
            hp_percentage_pokemon1 = 0.75
            hp_percentage_pokemon2 = 0.60

            self.screen.fill((0, 0, 0))  # Remplir l'écran avec une couleur de fond

            self.display_pokemon_sprites()
            self.display_hp_bars(hp_percentage_pokemon1, hp_percentage_pokemon2)
            self.display_text("C'est à votre tour ! Choisissez une action.")

            self.update_display()

            clock.tick(30)  # Limiter la fréquence d'images pour éviter une utilisation excessive du CPU

if __name__ == "__main__":
    battle_gui = GuiBattle()
    battle_gui.run_battle()

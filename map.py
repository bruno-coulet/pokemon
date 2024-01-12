from constants import *
from main_test import * # pg.init() et run = True

class Map(pg.sprite.Sprite):

    def __init__(self,x ,y):
        # appel la super classe pour initialiser le sprite
        super().__init__()
        # récupère le sprite sheet
        self.sprite_sheet = pg.image.load('assets/images/battle.png')
        # Récupère l'image générée ci-dessous avec def get_image
        self.image = self.get_image (0, 0)
        # rectangle de Position du sprite
        self.rect = self.image.get_rect()
        # différentes images du sprite 
        self.images = {
            'map_1' : self.get_image(0,0),
            'map_2' : self.get_image(259,0),
            'map_3' : self.get_image(518,0),
            'map_4' : self.get_image(774,0),
            'map_5' : self.get_image(0,0),
            'map_6' : self.get_image(259,0),
            'map_7' : self.get_image(518,0),
            'map_8' : self.get_image(774,0),
            'map_9' : self.get_image(0,0),
            'map_10' : self.get_image(259,0),
            'map_11' : self.get_image(518,0)
        }
        # Position du sprite dans la map
        self.position = [x, y]

        # Liste des maps
        self.map = ['map_1','map_2','map_3','map_4','map_5','map_6','map_7','map_8','map_9','map_10','map_11']

        # Choisi une vignette au hasard au début du jeu
        self.current_map = random.choice(self.map)
        self.change_map(self.current_map)

    def change_map(self, name):
        self.image = self.images[name]
    
    def get_image(self, x, y):
        full_screen = pg.Surface([800, 600])
        sprite_image = pg.Surface([258, 146])
        # Extrait une vignette du sprite_sheet
        sprite_image.blit(self.sprite_sheet, (0, 0), (x, y, 258, 146))
        # Agrandi la vignette
        pg.transform.scale(sprite_image, (800, 600), full_screen)
        # Retourne la vignette en 800 x 600 px
        return full_screen

map = Map(0, 0)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    pg.display.flip()
    fond = SCREEN.get_rect()
    SCREEN.blit(map.image, fond)
    pg.display.update()





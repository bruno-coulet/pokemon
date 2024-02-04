#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: pokedex.py

@project: Pokémon
@licence: GPLv3
"""
import random
import urllib.request
import requests
import os
import json
import time
from constants import POKEDEX_FILE, POKEDEX_SAVE, SP_POK_PATH, SP_TYP_PATH

"""Pour des question de droit, il a été décidé de ne pas stocker les images des pokemons dans le programme.
    C'est le joueur qui télécharge le pokedex en lançant le jeu"""
def init_db():
    """Initialise la base de donnée dans la variable data

    Returns: True ou reessaie 
    
    """
    url = "https://tyradex.tech/api/v1/pokemon"
    headers = {
        "User-Agent": "RobotPokemon",
        "From": "anonymous[at]laplateforme[dot]io",
        'Content-type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        with open(POKEDEX_FILE, 'w') as f:
            json.dump(data, f, indent=2)
            print("Initialized Pokedex DB successfully")
            return True
    else:
        print("The request failed with status code:", response.status_code)
        print("Retry connexion...")
        time.sleep(1)
        init_db()


class Pokedex:

    def __init__(self, save=None):
        """Verifie si le pokedex existe

        Attrs: save

        Sinon appel la fonction init_db()
        Si pokedex vide, ajoute  5 pokemons au hazard puis appel save_pokedex()
        Sinon appel load_pokedex()
        """
        if not os.path.isfile(POKEDEX_FILE):
            try:
                init_db()
            except Exception as e:
                print(f'Exception: {e}')
        else:
            print("Pokedex DB is already present.")


        if save is None:
            self.data = [None] * self.len_pokedex()
            for _ in range(5):
                self.add_pokemon(random.randint(1, 1017))
                time.sleep(0.5)
            self.save_pokedex()
            self.index_id = []
        else:
            self.data = self.load_pokedex(save)

    def add_pokemon(self, id_pok):
        """Ajoute un pokemon

        Attrs:
        -id_pok (int):

        Returns: charge les sprites regular, shiny et le type en.png
        
        appel la méthode save_pokedex (ci-dessous )
        
        """
        with open(POKEDEX_FILE, 'r') as f:
            if self.data[id_pok] is None:
                json_data = json.load(f)
                self.data[id_pok] = json_data[id_pok]
                if json_data[id_pok]['sprites']['regular'] is not None and not os.path.exists(f'{SP_POK_PATH}{id_pok}-regular.png'):
                    urllib.request.urlretrieve(json_data[id_pok]['sprites']['regular'], f'{SP_POK_PATH}{id_pok}-regular.png')
                    # wget.download(json_data[id_pok]['sprites']['regular'], out=f'{SP_POK_PATH}{id_pok}-regular.png')
                if json_data[id_pok]['sprites']['shiny'] is not None and not os.path.exists(f'{SP_POK_PATH}{id_pok}-shiny.png'):
                    urllib.request.urlretrieve(json_data[id_pok]['sprites']['shiny'],
                                               f'{SP_POK_PATH}{id_pok}-shiny.png')
                    # wget.download(json_data[id_pok]['sprites']['shiny'], out=f'{SP_POK_PATH}{id_pok}-shiny.png')
                for k in json_data[id_pok]['types']:
                    if not os.path.isfile(f'{SP_TYP_PATH}{k["name"]}.png'):
                        urllib.request.urlretrieve(k['image'], f'{SP_TYP_PATH}{k["name"]}.png')
                        # wget.download(k['image'], out=f'{SP_TYP_PATH}{k["name"]}.png')
        self.save_pokedex()


    def save_pokedex(self):
        """Ajoute le pokemon au pokedex

        Attrs: self

        Returns:  met à jour le fichier ./save/save.json'
        
        """
        filename = f'{POKEDEX_SAVE}'
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)

    def load_pokedex(self, filename):
        """Charge le pokedex
        
        Attrs: ./save/save.json'

        Returns: liste data avec les données de save.json
        
        """
        data = [None]
        with open(filename, 'r') as f:
            json_data = json.load(f)
            for k in range(1, self.len_pokedex()):
                if json_data[k] is None:
                    data.append(None)
                else:
                    data.append(json_data[k])
        return data

    @staticmethod
    def len_pokedex():
        """Longueur du pokedex

        Ouvre 'pokedex/pokedex.json'
        
        Returns: int longueur du pokedex
        """
        with open(POKEDEX_FILE, 'r') as f:
            json_data = json.load(f)
            return len(json_data)

    def count_pokemon(self):
        count = 0
        for k in self.data:
            if k is not None:
                count += 1
        return count

    def get_pokemon(self, id_pok):
        if self.data[id_pok] is not None:
            return self.data[id_pok]

    def read_pokedex(self):
        """Lis le pokedex
        
        Attrs: self
        
        Returns: liste pk_data
        """
        pok_data = []
        for k in self.data:
            if k is not None:
                pok_data.append(k)
        return pok_data

# PEUT-ON SUPPRIMER LE CODE CI-DESSOUS ?
# if __name__ == '__main__':
#     pass
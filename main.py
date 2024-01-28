#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: main.py

@project: Pokémon
@licence: GPLv3
"""
from pokedex import init_db
from constants import POKEDEX_FILE, SP_POK_PATH
import json
import os
import urllib.request
from game import Game


if __name__ == '__main__':
    # To please my friend
    init_db()
    with open(POKEDEX_FILE, 'r') as f:
        json_data = json.load(f)
        for id_pok in [112, 117, 138, 347, 402]:
            if json_data[id_pok]['sprites']['regular'] is not None and not os.path.exists(
                    f'{SP_POK_PATH}{id_pok}-regular.png'):
                urllib.request.urlretrieve(json_data[id_pok]['sprites']['regular'],
                                           f'{SP_POK_PATH}{id_pok}-regular.png')
                # wget.download(json_data[id_pok]['sprites']['regular'], out=f'{SP_POK_PATH}{id_pok}-regular.png')
            if json_data[id_pok]['sprites']['shiny'] is not None and not os.path.exists(
                    f'{SP_POK_PATH}{id_pok}-shiny.png'):
                urllib.request.urlretrieve(json_data[id_pok]['sprites']['shiny'],
                                           f'{SP_POK_PATH}{id_pok}-shiny.png')

    game = Game()
    game.run()

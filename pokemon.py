#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: pokemon.py

@project: Pokémon
@licence: GPLv3
"""


class Pokemon:
    def __init__(self, data: dict) -> None:
        self.id_pok = data['pokedexId']
        self.name = data['name']
        self.height = data['height']
        self.weight = data['weight']
        self.types = []
        for k in data['types']:
            self.types.append(k['name'])
        self.hp = data['stats']['hp']
        self.atk = data['stats']['atk']
        self.defense = data['stats']['def']
        self.spe_atk = data['stats']['spe_atk']
        self.spe_def = data['stats']['spe_def']
        self.speed = data['stats']['vit']
        self.resistances = []
        for k in data['resistances']:
            self.resistances.append((k['name'], k['multiplier']))
        self.level = 1
        self.evolution = data['evolution']['next']


if __name__ == '__main__':
    pass

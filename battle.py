#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: battle.py

@project: Pokémon
@licence: GPLv3
"""
from random import random, randint
from pokemon import Pokemon
from pokedex import Pokedex


class Battle:
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon, pokedex: Pokedex):
        self.p1 = pokemon1
        self.p1_name = pokemon1.name
        self.__p1_hp = pokemon1.hp
        self.p1_types = pokemon1.types
        self.__p1_atk = pokemon1.atk
        self.__p1_spe_atk = pokemon1.spe_atk
        self.p1_dfs = pokemon1.defense
        self.p1_spe_dfs = pokemon1.spe_def
        self.p1_res = pokemon1.resistances
        self.p1_speed = pokemon1.speed
        self.p1_level = pokemon1.level

        self.p2 = pokemon2
        self.p2_name = pokemon2.name
        self.__p2_hp = pokemon2.hp
        self.p2_types = pokemon2.types
        self.__p2_atk = pokemon2.atk
        self.__p2_spe_atk = pokemon2.spe_atk
        self.p2_dfs = pokemon2.defense
        self.p2_spe_dfs = pokemon2.spe_def
        self.p2_res = pokemon2.resistances
        if pokedex.get_pokemon(pokemon2.id_pok) is None:
            pokedex.add_pokemon(pokemon2.id_pok)

    def attack(self, attacker: Pokemon,  defender: Pokemon):
        pass

    def dodge(self, defender: Pokemon):
        pass

    def flee(self, defender: Pokemon):
        pass


if __name__ == '__main__':
    pass

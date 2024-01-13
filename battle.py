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
        self.__p1_hp = pokemon1.hp
        self.__p1_atk = pokemon1.atk
        self.__p1_spe_atk = pokemon1.spe_atk

        self.p2 = pokemon2
        self.__p2_hp = pokemon2.hp
        self.__p2_atk = pokemon2.atk
        self.__p2_spe_atk = pokemon2.spe_atk
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

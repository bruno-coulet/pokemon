#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: battle.py

@project: Pokémon
@licence: GPLv3
"""
from random import random
from pokemon import Pokemon
from pokedex import Pokedex
from math import log, sqrt


class Battle:
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon, pokedex: Pokedex):
        self.pokedex = pokedex

        self.p1 = pokemon1
        self.__p1_hp = pokemon1.hp
        self.__p1_atk = pokemon1.atk
        self.__p1_spe_atk = pokemon1.spe_atk

        self.p2 = pokemon2
        self.__p2_hp = pokemon2.hp
        self.__p2_atk = pokemon2.atk
        self.__p2_spe_atk = pokemon2.spe_atk

        self.__set_atk_pts()
        if pokedex.get_pokemon(pokemon2.id_pok) is None:
            self.pokedex.add_pokemon(pokemon2.id_pok)
            self.pokedex.save_pokedex()

    def __set_atk_pts(self):
        m1 = self.__set_coeff_atk(self.p1.types, self.p2.resistances)
        m2 = self.__set_coeff_atk(self.p2.types, self.p1.resistances)
        self.__p1_atk, self.__p1_spe_atk = round(self.__p1_atk * m1), round(self.__p1_spe_atk * m1)
        self.__p2_atk, self.__p2_spe_atk = round(self.__p2_atk * m2), round(self.__p2_spe_atk * m2)

    @staticmethod
    def __set_coeff_atk(types, resistances):
        m = 0
        count = 0
        for k in types:
            for resist in resistances:
                if k == resist[0]:
                    m += resist[1]
                    count += 1
        if m != 0:
            return m / count
        else:
            return 1

    def get_atk1(self):
        return self.__p1_atk

    def get_atk2(self):
        return self.__p2_atk

    def get_spe_atk1(self):
        return self.__p1_spe_atk

    def get_spe_atk2(self):
        return self.__p2_spe_atk

    def get_hp(self):
        return self.__p1_hp, self.__p2_hp

    def attack1(self, atk='atk'):
        match atk:
            case 'atk':
                if self.__p2_hp >= self.__p1_atk:
                    self.__p2_hp -= self.__p1_atk
                else:
                    self.__p2_hp = 0
            case 'spe':
                if self.__p2_hp >= self.__p1_spe_atk:
                    self.__p2_hp -= self.__p1_spe_atk
                else:
                    self.__p2_hp = 0

    def attack2(self, atk='atk'):
        match atk:
            case 'atk':
                if self.__p1_hp >= self.__p2_atk:
                    self.__p1_hp -= self.__p2_atk
                else:
                    self.__p1_hp = 0
            case 'spe':
                if self.__p1_hp >= self.__p2_spe_atk:
                    self.__p1_hp -= self.__p2_spe_atk
                else:
                    self.__p1_hp = 0

    @staticmethod
    def dodge(defender: Pokemon):
        chance_rate = log(1 + random() ** 3) * sqrt(defender.defense * defender.speed)
        if chance_rate > 20:
            return True
        else:
            return False

    def search_ko(self):
        x, y = self.get_hp()
        if x == 0 or y == 0:
            return True
        else:
            return False

    def damage_bar(self):
        return round(self.__p1_hp * 100 / self.p1.hp, 1), round(self.__p2_hp * 100 / self.p2.hp, 1)

    def flee(self):
        chance_rate = log(1 + random()) * self.p1.speed ** (1 / 3)
        print(chance_rate)
        if chance_rate > 2:
            return True
        else:
            return False

    def change_pok(self, pokemon: Pokemon):
        if pokemon.id_pok != self.p1.id_pok:
            self.p1 = pokemon
            self.__p1_hp = pokemon.hp
            self.__p1_atk = pokemon.atk
            self.__p1_spe_atk = pokemon.spe_atk
            self.__set_atk_pts()
            return True
        else:
            return False


if __name__ == '__main__':
    pass

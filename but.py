#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Bruno COULET, Cyril GENISSON
@file: but.py

@project: Pokémon
@licence: GPLv3
"""
from constants import *
import pygame as pg

BTN_WIDTH = 200
BTN_HEIGHT = 50
BTN_SIZE = (BTN_WIDTH, BTN_HEIGHT)
BTN_COLOR = COLORS['LIGHT_BLUE']
BTN_HOVER_COLOR = COLORS['DARK_BLUE']
BTN_TXT_COLOR = COLORS['WHITE']


class Text:
    def __init__(self, msg, position, clr=COLORS['CREME'], font="Segoe Print", font_size=15, mid=False):
        self.position = position
        self.font = pg.font.SysFont(font, font_size)
        self.txt_surf = self.font.render(msg, True, clr)

        if len(clr) == 4:
            self.txt_surf.set_alpha(clr[3])

        if mid:
            self.position = self.txt_surf.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.txt_surf, self.position)


class Button:
    def __init__(self, position, size, clr=COLORS['LIGHT_BLUE'], cngclr=COLORS['HOVER_COLOR'], func=None, text='',
                 font="Segoe Print", font_size=16, font_clr=COLORS['CREME']):
        self.clr = clr
        self.size = size
        self.func = func
        self.surf = pg.Surface(size)
        self.rect = self.surf.get_rect(center=position)

        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr

        if len(clr) == 4:
            self.surf.set_alpha(clr[3])

        self.font = pg.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, True, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

    def draw(self, screen):
        self.mouse_over()
        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouse_over(self):
        self.curclr = self.clr
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.curclr = self.cngclr

    def call_back(self, *args, **kwargs):
        if self.func:
            return self.func(*args, **kwargs)

        
class MenuButton(Button):
    def __init__(self, position, size=BTN_SIZE, clr=BTN_COLOR, cngclr=BTN_HOVER_COLOR, func=None, text='',
                 font=KANIT_BOLD, font_size=16, font_clr=BTN_TXT_COLOR):
        super().__init__(position, size, clr, cngclr, func, text, font, font_size, font_clr)
        # self.font = pg.font.SysFont(font, font_size)
        self.font = font

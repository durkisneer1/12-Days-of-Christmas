import pygame as pg
from constants import *


class Cookie:
    def __init__(self, parts_list):
        self.img = pg.image.load("res/cookie.png").convert_alpha()
        self.rect = self.img.get_rect(center=(WIN_WIDTH / 3, WIN_HEIGHT / 2))

        self.parts = parts_list
        self.showing = []

    def add_feature(self, index_val):
        self.showing.append(self.parts[index_val])
        self.parts.pop(index_val)

    def draw(self, screen: pg.Surface):
        screen.blit(self.img, self.rect)
        if self.showing:
            for parts in self.showing:
                screen.blit(parts, self.rect)

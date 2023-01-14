import pygame as pg
from random import randint
from constants import *


class Present:
    def __init__(self):
        img = pg.image.load("res/gift.png").convert_alpha()
        self.img = pg.transform.scale(img, (TILE_SIZE, TILE_SIZE))

        self.rect = self.img.get_rect()
        self.reposition()

    def reposition(self):
        self.rect.topleft = (randint(0, int(WIN_WIDTH / TILE_SIZE) - 1) * TILE_SIZE,
                             randint(0, int(WIN_HEIGHT / TILE_SIZE) - 1) * TILE_SIZE)

    def draw(self, screen: pg.Surface):
        screen.blit(self.img, self.rect)

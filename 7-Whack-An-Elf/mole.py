import pygame as pg
from random import randint
from constants import *


class Mole:
    def __init__(self):
        img = pg.image.load("res/elf_pop.png").convert_alpha()
        self.img = pg.transform.scale(img, (img.get_width() / 4,
                                            img.get_height() / 4))

        self.pos, self.rect = None, None
        self.reposition()

    def reposition(self):
        self.pos = (randint(0, WIN_WIDTH - self.img.get_width()),
                    randint(0, WIN_HEIGHT - self.img.get_height()))
        self.rect = self.img.get_rect(topleft=self.pos)

    def draw(self, screen: pg.Surface):
        screen.blit(self.img, self.pos)

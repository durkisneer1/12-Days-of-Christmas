import pygame as pg
from constants import *


class Counter:
    def __init__(self):
        self.font = pg.font.SysFont("comicsans", 42)
        self.points = 0

        self.text = self.font.render(f"{self.points}", False, "black")
        self.pos = (WIN_WIDTH * (3/4), WIN_HEIGHT / 6)
        self.text_box = self.text.get_rect(center=self.pos)

    def add(self):
        self.points += 1
        self.text = self.font.render(f"{self.points}", False, "black")
        self.text_box = self.text.get_rect(center=self.pos)

    def draw(self, screen: pg.Surface):
        screen.blit(self.text, self.text_box)

import pygame as pg
from math import sin
from random import randint
from constants import *


class TemplateWave:
    def __init__(self):
        scale = 5
        self.amplitude = randint(1, 9) * scale
        self.stretch = randint(1, 9) * scale
        self.points = self.calculate()

    def give_attr(self):
        return self.amplitude, self.stretch

    def calculate(self):
        points = []
        for i in range(int(WIN_WIDTH / 2)):
            points.append((i + WIN_WIDTH / 4, sin(i / self.stretch) * self.amplitude + (WIN_HEIGHT / 2)))
        return points

    def draw(self, screen: pg.Surface):
        pg.draw.lines(screen, "black", False, self.points, 7)
        pg.draw.lines(screen, "red", False, self.points, 3)

import pygame as pg
from math import sin
from random import randint
from constants import *


class MatchWave:
    def __init__(self):
        self.scale = 5
        self.amplitude = randint(1, 9) * self.scale
        self.stretch = randint(1, 9) * self.scale
        self.points = self.calculate()

    def give_attr(self):
        return self.amplitude, self.stretch

    def calculate(self):
        points = []
        for i in range(int(WIN_WIDTH / 2)):
            points.append((i + WIN_WIDTH / 4, sin(i / self.stretch) * self.amplitude + (WIN_HEIGHT / 2)))
        return points

    def edit_amp(self, amplitude):
        self.amplitude = amplitude * self.scale
        self.points = self.calculate()

    def edit_stretch(self, stretch):
        self.stretch = stretch * self.scale
        self.points = self.calculate()

    def draw(self, screen: pg.Surface):
        pg.draw.lines(screen, "lightgray", False, self.points, 5)
        pg.draw.lines(screen, "blue", False, self.points, 3)

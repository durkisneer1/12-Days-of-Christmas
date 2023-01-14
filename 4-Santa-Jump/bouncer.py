import pygame as pg
from random import choice, randint
from constants import *


class BouncePlatform(pg.sprite.Sprite):
    def __init__(self, groups: list[pg.sprite.Group], y_pos):
        super().__init__(groups)  # NOQA

        self.surf = pg.image.load("res/cane.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.pos = pg.Vector2(randint(0, WIN_WIDTH - self.surf.get_width()), y_pos)

        self.right = choice([True, False])
        self.speed = randint(5, 10)

    def move(self, dt):
        self.rect.topleft = self.pos

        if self.right:
            self.pos.x += self.speed * dt
        else:
            self.pos.x -= self.speed * dt

        if self.pos.x > WIN_WIDTH - self.surf.get_width():
            self.pos.x = WIN_WIDTH - self.surf.get_width()
            self.speed *= -1
        elif self.pos.x < 0:
            self.pos.x = 0
            self.speed *= -1

        self.pos.y %= WIN_HEIGHT

    def draw(self, screen: pg.Surface):
        screen.blit(self.surf, self.pos)

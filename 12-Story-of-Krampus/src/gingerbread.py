import pygame as pg

from .settings import *


class Gingerbread:
    og_speed = 2

    def __init__(self):
        self.img = pg.image.load("assets/monsters/gingerbread.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.pos = pg.Vector2(WIN_WIDTH / 2 - 1, WIN_HEIGHT / 2)

        self.speed = self.og_speed
        self.hittable = False

    def move(self, dt):
        self.rect.center = self.pos
        self.pos.y += self.speed * dt
        if self.pos.y > 65:
            self.hittable = True
        else:
            self.hittable = False

    def attack(self) -> bool:
        return self.rect.bottom > WIN_HEIGHT - 6  # Bottom of chimney

    def draw(self, screen):
        screen.blit(self.img, self.rect)

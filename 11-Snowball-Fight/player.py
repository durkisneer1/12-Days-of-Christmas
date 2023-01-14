import pygame as pg
from constants import *


class Player:
    def __init__(self, player_type):
        self.type = player_type
        self.health = 3

        img = pg.image.load("res/cannon.png").convert_alpha()
        img = pg.transform.scale(
            img, (img.get_width() / 2, img.get_height() / 2)
        )

        self.img = pg.transform.flip(img, True, False) if player_type == 1 else img
        self.rect = self.img.get_rect()

        pos = (0, 0) if player_type == 1 else\
            (WIN_WIDTH - self.rect.width, WIN_HEIGHT - self.rect.height)
        self.pos = pg.Vector2(pos)

        self.speed = 20

    def move(self, keys, dt):
        self.rect.topleft = self.pos

        if self.type == 1:
            if keys[pg.K_w]:
                self.pos.y -= self.speed * dt
            elif keys[pg.K_s]:
                self.pos.y += self.speed * dt
        elif self.type == 2:
            if keys[pg.K_UP]:
                self.pos.y -= self.speed * dt
            elif keys[pg.K_DOWN]:
                self.pos.y += self.speed * dt

        if self.pos.y < 0:
            self.pos.y = 0
        elif self.pos.y > WIN_HEIGHT - self.rect.height:
            self.pos.y = WIN_HEIGHT - self.rect.height

    def draw(self, screen):
        screen.blit(self.img, self.rect)

import pygame as pg
from constants import *


class Player:
    def __init__(self):
        img = pg.image.load("res/grinch.png").convert_alpha()
        self.img = pg.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.img.get_rect()

        self.pos = pg.Vector2(0, 0)
        self.direction = pg.Vector2()
        self.move_tick = 0
        self.speed = 2

    def move(self, dt, events):
        self.rect.topleft = self.pos

        for ev in events:
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_w:
                    self.direction.xy = 0, -1
                elif ev.key == pg.K_s:
                    self.direction.xy = 0, 1
                elif ev.key == pg.K_a:
                    self.direction.xy = -1, 0
                elif ev.key == pg.K_d:
                    self.direction.xy = 1, 0

        self.move_tick += dt * self.speed
        if self.move_tick > 1:
            self.pos += self.direction * TILE_SIZE
            self.move_tick = 0

    def bound(self):
        return (self.pos.x < -TILE_SIZE or
                self.pos.x > WIN_WIDTH or
                self.pos.y < -TILE_SIZE or
                self.pos.y > WIN_HEIGHT)

    def draw(self, screen):
        screen.blit(self.img, self.pos)

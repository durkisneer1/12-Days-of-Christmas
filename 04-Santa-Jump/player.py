import pygame as pg
from constants import *


class Player(pg.sprite.Sprite):
    def __init__(self, groups: pg.sprite.Group):
        super().__init__(groups)

        self.img_list = [pg.image.load("res/santa/up.png").convert_alpha(),
                         pg.image.load("res/santa/down.png").convert_alpha()]
        self.img = self.img_list[0]
        self.rect = self.img.get_rect()
        self.pos = pg.Vector2(WIN_WIDTH / 2, WIN_HEIGHT)

        self.up = False
        self.ready = False
        self.grav = 20
        self.jump = 80
        self.vel = 0
        self.speed = 40

    def bounce(self):
        self.vel = self.jump

    def move(self, dt, keys):
        self.rect.bottomleft = self.pos

        if self.ready:
            self.vel -= self.grav * dt
            self.pos.y -= self.vel * dt
        else:
            if keys[pg.K_SPACE]:
                self.bounce()
                self.ready = True

        if keys[pg.K_a]:
            self.pos.x -= self.speed * dt
        if keys[pg.K_d]:
            self.pos.x += self.speed * dt

    def get_direction(self):
        if self.vel > 0:
            self.up = True
            self.img = self.img_list[0]
        else:
            self.up = False
            self.img = self.img_list[1]

    def dead(self):
        return self.pos.y > WIN_HEIGHT

    def draw(self, screen: pg.Surface):
        screen.blit(self.img, self.rect)

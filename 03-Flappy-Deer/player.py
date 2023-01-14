import pygame as pg
from constants import *


class Santa:
    def __init__(self):
        img = pg.image.load("res/santa.png")
        self.img = pg.transform.scale(img, (img.get_width() / 3, img.get_height() / 3)).convert_alpha()
        self.pos = pg.Vector2(WIN_WIDTH / 6, WIN_HEIGHT / 2)
        self.angle = 0

        self.rot_img = pg.transform.rotate(self.img, self.angle)
        self.rect = self.rot_img.get_rect()
        self.mask = None

        self.vel = -50
        self.grav = 15

    def rotate(self, dt):
        if self.angle > -30:
            self.angle -= 10 * dt
        else:
            self.angle = -30

    def jump(self, events, dt):
        for ev in events:
            if ev.type == pg.KEYDOWN and ev.key == pg.K_SPACE:
                self.angle = 30
                self.vel = -50

        self.pos.y += self.vel * dt
        self.vel += self.grav * dt

        self.rect = self.rot_img.get_rect()
        self.rect.center = self.pos
        self.mask = pg.mask.from_surface(self.img)

    def bound(self):
        if self.pos.y < 0:
            self.pos.y = 0

    def draw(self, screen):
        self.rot_img = pg.transform.rotate(self.img, self.angle)
        screen.blit(self.rot_img, self.rect)


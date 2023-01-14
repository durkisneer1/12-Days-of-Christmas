import pygame as pg

from .settings import *


class Jumpscare:
    def __init__(self, img):
        self.img = img
        self.pos = pg.Vector2(WIN_WIDTH / 2, WIN_HEIGHT / 2)
        self.rect = self.img.get_rect(center=self.pos)
        self.scaler = 0.1

        self.scaled_img = self.img

    def update(self, dt):
        self.scaler += dt
        self.scaled_img = pg.transform.scale_by(self.img, self.scaler)
        self.rect = self.scaled_img.get_rect(center=self.pos)

    def draw(self, screen):
        screen.blit(self.scaled_img, self.rect)

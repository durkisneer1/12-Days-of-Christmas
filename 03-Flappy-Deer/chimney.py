import pygame as pg
from constants import *


class Chimney(pg.sprite.Sprite):
    def __init__(self, groups: pg.sprite.Group, top: bool, random_height, img):
        super().__init__(groups)

        height = -random_height - 200 if top else WIN_HEIGHT - random_height + 100

        self.img = img if not top else pg.transform.flip(img, False, True)
        self.rect = self.img.get_rect()
        self.mask = None

        self.pos = pg.Vector2(WIN_WIDTH, height)
        self.speed = 20

    def move(self, dt):
        self.rect.topleft = self.pos
        self.pos.x -= self.speed * dt

        if self.pos.x < -self.img.get_width():
            self.kill()

        self.mask = pg.mask.from_surface(self.img)

    def draw(self, screen):
        screen.blit(self.img, self.pos)

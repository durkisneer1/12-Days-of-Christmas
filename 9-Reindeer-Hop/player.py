import pygame as pg
from constants import *


class Player:
    def __init__(self, ground_rect):
        self.ground = ground_rect

        self.frame_list = [pg.transform.scale(
            pg.image.load(f"res/santa_anim/{i}.png"),
            (32, 32)).convert_alpha() for i in range(12)]

        self.current_frame = 0
        self.img = self.frame_list[self.current_frame]
        self.rect = self.img.get_rect()
        self.mask = pg.mask.from_surface(self.img)
        self.pos = pg.Vector2(WIN_WIDTH / 4, WIN_HEIGHT * 3 / 4)

        self.vel = 0
        self.jump = 50
        self.grav = 20
        self.on_ground = True

        self.lives = 3

    def animate(self, dt):
        self.current_frame += dt * 2
        try:
            self.img = self.frame_list[int(self.current_frame)]
            self.mask = pg.mask.from_surface(self.img)
        except IndexError:
            self.current_frame = 0

    def move(self, keys, dt):
        self.rect.bottomleft = self.pos

        if not self.on_ground:
            self.vel -= self.grav * dt
            self.pos.y -= self.vel * dt
        else:
            if keys[pg.K_SPACE]:
                self.vel = self.jump
                self.on_ground = False

        if self.rect.bottom > self.ground.top:
            self.pos.y = self.ground.top
            self.on_ground = True

    def draw(self, screen):
        screen.blit(self.img, self.rect)
import pygame as pg

from .settings import *
from .flashlight import Flashlight
from .jumpscare import Jumpscare
from .gingerbread import Gingerbread
from .clown import Clown


def create_scare(path) -> Jumpscare:
    img = pg.image.load(path).convert_alpha()
    return Jumpscare(img)


class Scene:
    def __init__(self):
        self.blank = pg.Surface((WIN_WIDTH, WIN_HEIGHT), pg.SRCALPHA)
        self.light = Flashlight()

        self.chimney = pg.image.load("assets/decor/chimney.png").convert_alpha()
        self.bread = Gingerbread()
        self.clown = Clown()

        self.bread_scare = create_scare("assets/jumpscares/gingerbread.png")
        self.clown_scare = create_scare("assets/monsters/clown/4.png")

        self.scare_time = 0
        self.current_time = 0
        self.dead = False

    def light_push(self, dt, mouse_pressed):
        mouse_pos = pg.mouse.get_pos()

        if (
            mouse_pressed[0]
            and self.bread.rect.collidepoint(mouse_pos)
            and self.bread.hittable
            and self.light.active
        ):
            self.bread.speed = -5
        else:
            self.bread.speed = self.bread.og_speed

        if (
            mouse_pressed[0]
            and self.clown.rect.collidepoint(mouse_pos)
            and self.clown.hittable
            and self.light.active
        ):
            self.clown.current_frame -= dt / 2

    def attack_handler(self, dt):
        if self.bread.attack():
            self.bread_scare.update(dt)
            if self.current_time - self.scare_time > 1000:
                self.dead = True
        elif self.clown.attack:
            self.clown_scare.update(dt)
            if self.current_time - self.scare_time > 1000:
                self.dead = True
        else:
            self.scare_time = self.current_time

    def update(self, dt):
        mouse_pressed = pg.mouse.get_pressed()
        self.current_time = pg.time.get_ticks()
        self.light.update(mouse_pressed)

        self.clown.update(dt)
        self.bread.move(dt)

        self.light_push(dt, mouse_pressed)
        self.attack_handler(dt)

    def draw(self, screen):
        self.blank.fill((0, 0, 0, 150))

        self.clown.draw(screen)
        self.bread.draw(screen)

        screen.blit(self.chimney, (0, 0))

        if self.bread.attack():
            self.bread_scare.draw(screen)
        elif self.clown.attack:
            self.clown_scare.draw(screen)

        self.light.draw(self.blank)
        screen.blit(self.blank, (0, 0))

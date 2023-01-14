import pygame as pg


class Clown:
    def __init__(self):
        self.frame_list = [
            pg.image.load(f"assets/monsters/clown/{i}.png").convert() for i in range(5)
        ]
        self.current_frame = 0

        self.img = self.frame_list[self.current_frame]
        self.rect = self.img.get_rect(topleft=(13, 10))

        self.hittable = False
        self.attack = False

    def update(self, dt):
        self.current_frame += dt / 4
        if self.current_frame > len(self.frame_list):
            self.attack = True
        else:
            self.img = self.frame_list[int(self.current_frame)]

        if self.current_frame > 0:
            self.hittable = True

    def draw(self, screen):
        screen.blit(self.img, self.rect)

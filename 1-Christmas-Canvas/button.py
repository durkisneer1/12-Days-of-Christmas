import pygame as pg


class Button:
    def __init__(self, font):
        self.surf = pg.Surface((100, 50))
        self.rect = self.surf.get_rect(topleft=(0, 0))

        self.text = font.render("CLEAR", True, "white")
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        screen.blit(self.text, self.text_rect)

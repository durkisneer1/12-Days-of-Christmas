import pygame as pg


class Card(pg.sprite.Sprite):
    def __init__(self, group: pg.sprite.Group, img: pg.Surface, card_type: int, pos: tuple):
        super().__init__(group)
        self.cover = pg.image.load("res/card_cover.png").convert()
        self.img = img.copy()
        self.type = card_type
        self.current_card = self.cover

        self.rect = self.img.get_rect(topleft=pos)
        self.flipped = False

    def user_input(self, events):
        for ev in events:
            if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:
                if self.rect.collidepoint(ev.pos):
                    self.flipped = not self.flipped

    def draw(self, screen: pg.Surface):
        # Change card image
        self.current_card = self.img if self.flipped else self.cover
        screen.blit(self.current_card, self.rect)

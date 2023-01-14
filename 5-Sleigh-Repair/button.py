import pygame as pg


class Button:
    def __init__(self, img: pg.Surface, pos: tuple, message: str):
        self.surf = pg.transform.scale(img, (200, 100))
        self.rect = self.surf.get_rect(midtop=pos)

        font = pg.font.SysFont("comicsans", 42)
        self.text = font.render(message, True, "black")
        self.text_box = self.text.get_rect(center=self.rect.center)

        self.outline_color = "black"

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.outline_color, ((self.rect.x - 3, self.rect.y - 3),
                                                  (self.rect.w + 6, self.rect.h + 6)))
        screen.blit(self.surf, self.rect)
        screen.blit(self.text, self.text_box)

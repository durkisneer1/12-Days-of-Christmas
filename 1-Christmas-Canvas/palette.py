import pygame as pg


class ColorPalette(pg.sprite.Sprite):
    def __init__(self, groups: pg.sprite.Group, color: str, pos: tuple, selection: int):
        super().__init__(groups)
        self.surf = pg.Surface((50, 50))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=pos)

        font = pg.font.SysFont("Helvetica", 24)
        self.text = font.render(f"{selection}", True, "black")
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        screen.blit(self.text, self.text_rect)

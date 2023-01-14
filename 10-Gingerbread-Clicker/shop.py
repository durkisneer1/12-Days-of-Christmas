import pygame as pg


class Item(pg.sprite.Sprite):
    def __init__(self,
                 group: pg.sprite.Group,
                 color: int,
                 pos: tuple,
                 value: int,
                 img: pg.Surface):

        super().__init__(group)
        self.value = value
        self.color = (color, color, color)
        font = pg.font.SysFont("comicsans", 36)

        self.surf = pg.transform.scale(img, (100, 60))
        self.rect = self.surf.get_rect(midbottom=pos)
        self.text = font.render(f"{value}", False, "black")

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.surf, self.rect)
        screen.blit(self.text, self.rect.topright)

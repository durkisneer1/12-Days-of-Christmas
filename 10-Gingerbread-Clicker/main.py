import pygame as pg
from constants import *
from cookie import Cookie
from counter import Counter
from shop import Item

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Gingerbread Clicker")

cookie_items = [pg.image.load("res/bowtie.png").convert_alpha(),
                pg.image.load("res/buttons.png").convert_alpha(),
                pg.image.load("res/face.png").convert_alpha(),
                pg.image.load("res/lines.png").convert_alpha()]

cookie = Cookie(cookie_items)
counter = Counter()
item_group = pg.sprite.Group()
for i in range(len(cookie_items)):
    Item(item_group,
         int(255 / (i + 1)),
         (WIN_WIDTH - WIN_WIDTH / 4, (i * 60) + WIN_HEIGHT / 2),
         (i + 1) * 25,
         cookie_items[i])


def main():
    num_complete = 0
    run = True
    while run:
        for ev in pg.event.get():
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False
            if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:
                if cookie.rect.collidepoint(ev.pos):
                    counter.add()
                for index, item in enumerate(item_group):
                    if item.rect.collidepoint(ev.pos) and counter.points >= item.value:
                        cookie.add_feature(index)
                        counter.points -= item.value
                        num_complete += 1
                        item.kill()

        screen.fill("lightblue")
        cookie.draw(screen)
        counter.draw(screen)
        for item in item_group:
            item.draw(screen)

        pg.display.flip()


if __name__ == '__main__':
    main()

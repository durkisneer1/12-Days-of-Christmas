import pygame as pg
from math import floor
from constants import *
from mole import Mole

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pg.SCALED)
pg.display.set_caption("Whack An Elf")
clock = pg.time.Clock()

font = pg.font.SysFont("comicsans", 16)
bg_img = pg.image.load("res/background.png").convert()
bg_img = pg.transform.scale(bg_img, (WIN_WIDTH, WIN_HEIGHT))

mole = Mole()


def main():
    current_points = 0
    game_over = False
    run = True
    while run:
        for ev in pg.event.get():
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False

            if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1 and not game_over:
                if mole.rect.collidepoint(ev.pos):
                    current_points += 1
                    mole.reposition()

        current_time = pg.time.get_ticks()
        time_left = 20
        time_left -= floor(current_time / 1000)
        show_time = font.render(f"Time Remaining: {time_left}", False, "black")

        show_points = font.render(f"Whacks: {current_points}", False, "black")
        game_over = True if time_left < 0 else False

        screen.blit(bg_img, (0, 0))
        if not game_over:
            mole.draw(screen)
            screen.blit(show_time, (10, 5))
            screen.blit(show_points, (WIN_WIDTH - show_points.get_width() - 10, 5))
        else:
            total_points = font.render(f"Time Is Up! You made {current_points} points!", False, "black")
            screen.blit(total_points, ((WIN_WIDTH / 2) - (total_points.get_width() / 2),
                                       (WIN_HEIGHT / 2) - (total_points.get_height() / 2)))

            press_close = font.render("Press ESC To Close.", False, "black")
            screen.blit(press_close, ((WIN_WIDTH / 2) - (press_close.get_width() / 2),
                                      WIN_HEIGHT - 100))

        pg.display.flip()


if __name__ == '__main__':
    main()

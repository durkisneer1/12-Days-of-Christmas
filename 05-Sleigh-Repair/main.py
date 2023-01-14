import pygame as pg
from constants import *
from template import TemplateWave
from match import MatchWave
from button import Button

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Sleigh Repair")

background = pg.image.load("res/sled_bg.jpg").convert()
plate = pg.image.load("res/plate.jpg").convert()
tablet = pg.image.load("res/black screen.png").convert()

template_wave = TemplateWave()
match_wave = MatchWave()

selections_dict = {eval(f"pg.K_{i}"): i for i in range(1, 9 + 1)}
amp_button = Button(plate, (WIN_WIDTH / 3, 25), "Amplitude")
stretch_button = Button(plate, (WIN_WIDTH - WIN_WIDTH / 3, 25), "Stretch")


def main():
    edit_mode = [False, False]
    run = True
    while run:
        mouse_pos = pg.mouse.get_pos()
        mouse_input = pg.mouse.get_pressed()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                run = False
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    run = False

                if ev.key in range(pg.K_1, pg.K_9 + 1):
                    if edit_mode[0]:
                        match_wave.edit_amp(selections_dict[ev.key])
                    elif edit_mode[1]:
                        match_wave.edit_stretch(selections_dict[ev.key])

                    if template_wave.give_attr() == match_wave.give_attr():
                        template_wave.__init__()

        if mouse_input[0]:
            if amp_button.rect.collidepoint(mouse_pos):
                edit_mode = [True, False]
                amp_button.outline_color = "yellow"
                stretch_button.outline_color = "black"
            elif stretch_button.rect.collidepoint(mouse_pos):
                edit_mode = [False, True]
                stretch_button.outline_color = "yellow"
                amp_button.outline_color = "black"

        screen.blit(background, (0, 0))
        screen.blit(plate, (100, WIN_HEIGHT / 2 - 100))
        screen.blit(tablet, (WIN_WIDTH / 4, WIN_HEIGHT / 2 - 45))

        template_wave.draw(screen)
        match_wave.draw(screen)

        amp_button.draw(screen)
        stretch_button.draw(screen)

        pg.display.flip()


if __name__ == '__main__':
    main()

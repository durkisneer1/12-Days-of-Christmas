import pygame as pg
import numpy as np
from button import Button
from palette import ColorPalette


# Window Initialization
pg.init()
WIN_WIDTH, WIN_HEIGHT = 1200, 900
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Christmas Canvas")
font = pg.font.SysFont("Helvetica", 24)

# Tile canvas
tile_size = 10
tile_grid = int(WIN_WIDTH / tile_size), int(WIN_HEIGHT / tile_size)
canvas = np.zeros(tile_grid, np.intc)

# Color Search
current_color = pg.K_1
color_dict = {pg.K_1: "blue", pg.K_2: "red", pg.K_3: "green", pg.K_4: "orange", pg.K_5: "purple"}
color_pick = font.render(f"{color_dict[current_color]}", True, "black", "white")

# Instancing
button = Button(font)
palette_group = pg.sprite.Group()
x_offset = 0
label = 1
for i in range(pg.K_1, pg.K_5 + 1):
    ColorPalette(palette_group, color_dict[i], (x_offset + button.rect.topright[0], 0), label)
    x_offset += 50
    label += 1


run = True
while run:
    m_input = pg.mouse.get_pressed()
    raw_m_pos = pg.Vector2(pg.mouse.get_pos())

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            run = False
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                run = False

            # Color switching
            current_color = ev.key
            color_pick = font.render(f"{color_dict.get(current_color)}", True, "black", "white")

        # Clear button
        if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:
            if button.rect.collidepoint(raw_m_pos):
                for pos, value in np.ndenumerate(canvas):
                    canvas[pos[0]][pos[1]] = 0

    # Bound cursor from max index
    m_pos = raw_m_pos / tile_size
    if m_pos.x > WIN_WIDTH / tile_size - 0.1:
        m_pos.x = WIN_WIDTH / tile_size - 0.1
    elif m_pos.x < 0:
        m_pos.x = 0
    if m_pos.y > WIN_HEIGHT / tile_size - 0.1:
        m_pos.y = WIN_HEIGHT / tile_size - 0.1
    elif m_pos.y < 0:
        m_pos.y = 0

    # Drawing
    screen.fill("lightgray")
    for pos, value in np.ndenumerate(canvas):
        draw_pos = pos[0] * tile_size, pos[1] * tile_size
        if m_input[0]:
            canvas[int(m_pos[0])][int(m_pos[1])] = current_color
        if value != 0 and color_dict.get(value) is not None:
            pg.draw.rect(screen, color_dict.get(value), (draw_pos, (tile_size, tile_size)))

    for color in palette_group:
        color.draw(screen)
    button.draw(screen)
    screen.blit(color_pick, (1, WIN_HEIGHT - color_pick.get_height() - 1))

    # Refresh
    pg.display.flip()

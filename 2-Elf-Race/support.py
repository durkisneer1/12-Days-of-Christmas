from os import walk
import pygame as pg


def import_folder(path: str) -> list[pg.Surface]:
    surf_list = []
    for _, __, img_list in walk(path):
        for img in img_list:
            full_path = path + '/' + img
            img_surf = pg.image.load(full_path).convert_alpha()
            surf_list.append(img_surf)
    return surf_list

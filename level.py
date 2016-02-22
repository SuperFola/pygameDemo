__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import os
import pygame
from glob import glob

from constantes import *


class Level:
    def __init__(self, default_map=None):
        self.default_map = default_map if default_map else DEFAULT_MAP
        self.sprites = {os.path.split(path)[1].replace('.png', ''): pygame.image.load(path).convert_alpha() for path in glob("tiles/*.png")}

    def get_map_size(self):
        # toutes les lignes sont censées faire la même taille
        return len(self.default_map[0]), len(self.default_map)

    def get_block_at(self, x, y):
        # on utilise une double liste
        return self.default_map[y][x]

    def load(self):
        pass

    def save(self):
        pass
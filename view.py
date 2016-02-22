__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import pygame

from constantes import *


class View:
    def __init__(self, player, level):
        self.player = player
        self.level = level

    def draw(self, surface):
        pygame.draw.rect(surface, SKYBOX_COLOR, (0, 0) + surface.get_size())

        surface.blit(self.player.sprite, self.player.pos)

        # affiche de la map
        for y in range(self.level.get_map_size()[1]):
            for x in range(self.level.get_map_size()[0]):
                tile_code = self.level.get_block_at(x, y)
                surface.blit(self.level.sprites[tile_code], (x * TILE_SIZE, y * TILE_SIZE))
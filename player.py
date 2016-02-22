__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import pygame

from constantes import *


class Player:
    def __init__(self, start_pos, speed=5):
        self.pos = start_pos
        self.speed = speed
        # il faut convertir l'image en un format lisible par Pygame
        self.sprite = pygame.image.load("player.png").convert_alpha()

    def move(self, direction):
        x, y = self.pos  # on ne pas modifier directement un tuple, donc on unpack

        if direction == UP:
            # origine en haut à gauche ! Faire attention donc :)
            y -= self.speed
        if direction == DOWN:
            y += self.speed
        if direction == RIGHT:
            x += self.speed
        if direction == LEFT:
            x -= self.speed

        self.pos = x, y

    def load(self):
        pass

    def save(self):
        pass
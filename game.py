__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import pygame
from pygame.locals import *

from constantes import *
import view
import player
import level


class Game:
    def __init__(self, window):
        self.window = window
        self.running = True
        self.player = player.Player((0, 0))
        self.level = level.Level()
        self.view = view.View(self.player, self.level)

    def prepare(self):
        self.running = True
        # c'est 2 méthodes ne font rien, à vous de les implémenter correctement :)
        self.player.load()
        self.level.load()

    def render(self):
        self.view.draw(self.window)

    def save(self):
        # c'est deux méthodes ne font rien non plus, à vous de les implémenter :)
        self.player.save()
        self.level.save()

    def process_event(self, event):
        if event.type == QUIT:
            self.running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.player.move(RIGHT)
            if event.key == K_LEFT:
                self.player.move(LEFT)
            if event.key == K_UP:
                self.player.move(UP)
            if event.key == K_DOWN:
                self.player.move(DOWN)

    def run(self):
        self.prepare()

        while self.running:
            self.process_event(pygame.event.poll())

            self.render()

            pygame.display.flip()

        self.save()
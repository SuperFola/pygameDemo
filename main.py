__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import pygame
from pygame.locals import *

from constantes import *
import game


class Main:
    def __init__(self):
        # initialisation de pygame et de font (ici je n'écris rien sur l'écran, c'est une habitude)
        pygame.init()
        pygame.font.init()
        # création de la fenetre
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        # creation de la police
        self.font = pygame.font.SysFont("arial", 18)
        # boolean pour savoir si on continue ou pas
        self.running = True

    def prepare(self):
        # répétition des touches, à partir de 200ms d'appui, toutes les 100ms
        pygame.key.set_repeat(200, 100)
        # si jamais on relance le menu juste apres, self.running vaudra False, donc on le remet à True
        self.running = True

    def process_event(self, event):
        # si on a cliqué sur la croix de la fenetre
        if event.type == QUIT:
            self.running = False
        # on appuie sur une touche (appui toujours en cours)
        # utiliser KEYUP pour savoir si on vient de relacehr une touche
        if event.type == KEYDOWN:
            if event.key == K_j:
                playground = game.Game(self.window)
                playground.run()

    def render(self):
        # on dessine un rectangle noir qui prend tout l'écran
        # il commence en 0, 0 et width, height = self.window.get_size()
        # ATTENTION
        # l'origine du répère est en haut à gauche de la fenêtre !!
        pygame.draw.rect(self.window, BLACK, (0, 0) + self.window.get_size())

    def run(self):
        self.prepare()

        while self.running:
            self.process_event(pygame.event.poll())  # on prend un événement de la queue des événéments
            #  on l'envoie à la fonction pour le traiter

            # dessin
            self.render()

            # actualisation de l'écran
            pygame.display.flip()

        pygame.quit()  # toujours désalouer toute la mémoire utilisée


# code d'exemple pour créer un texte et l'afficher :
# color est un tuple de 3 éléments
# text = self.font.render(text, 1, color)
# affichage sur l'écran :
# self.window.blit(text, pos)
# pos est un tuple ou une liste de 2 éléments, x et y

if __name__ == '__main__':
    menu = Main()
    menu.run()
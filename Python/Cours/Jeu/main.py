import pygame
import sys
from ball import Ball

class Game:

    def __init__(self):
        pygame.init()

        # Définir les dimensions de la fenêtre
        self.screen_width = 800
        self.screen_height = 600
        black=(0,0,0)
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Aller-Retour d'une Balle")


        en_cours = True
        clock = pygame.time.Clock()

        ball_list=[]

        for i in range(5000):
            ball_list.append(Ball(self))



        while en_cours:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

            for ball in ball_list:
                ball.draw(screen)
                ball.move(self.screen_width, self.screen_height)

            pygame.display.flip()

            clock.tick(60)

        # Quitter pygame
        pygame.quit()
        sys.exit()

Game()
import pygame
import sys
from Config import Config
from obstacle import Obstacle

from Cours.Bomberman import hero
from Cours.Bomberman.obstacle import Obstacle
from hero import Hero

# Initialiser pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen = pygame.display.set_mode((Config.screen_width, Config.screen_height))
pygame.display.set_caption("Bomberman")

running = True
clock = pygame.time.Clock()

JohnWo = Hero(200, 200, 50, 15)
obstacle = Obstacle(500, 550)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    keys = pygame.key.get_pressed()
    JohnWo.move(screen, obstacle, keys)

    # Remplir l'écran et dessiner la balle
    screen.fill((255, 255, 255))
    JohnWo.draw(screen)
    obstacle.draw(screen)

    # Rafraîchir l'affichage
    pygame.display.flip()

    # Contrôler la vitesse de la boucle
    clock.tick(60)

# Quitter pygame
pygame.quit()
sys.exit()

import pygame
from Config import Config


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (125, 125, 125)
        self.hitbox= (self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, rect=(self.x, self.y, self.width, self.height))

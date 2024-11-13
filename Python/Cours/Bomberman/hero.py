import pygame
from Config import Config
from pygame.rect import RectType


class Hero:

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, screen):
        return pygame.draw.rect(screen, (0, 0, 0), rect=(self.x, self.y, self.width, self.height))

    def move(self, screen, obstacle, keys):

        if keys[pygame.K_DOWN] and self.y + self.height < Config.screen_height:

            self.y += 10
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 10
        if keys[pygame.K_RIGHT] and self.x + self.width < Config.screen_width:
            self.x += 10
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 10

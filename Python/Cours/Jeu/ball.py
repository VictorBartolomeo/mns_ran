import pygame
import random

class Ball :

    def __init__(self, game):
        self.rayon= random.uniform(0.1,3)
        self.x=random.uniform(self.rayon,game.screen_width-self.rayon)
        self.y=random.uniform(self.rayon,game.screen_height-self.rayon)
        self.speed_x= random.uniform(0.1,4)
        self.speed_y= random.uniform(0.1,4)
        self.color = (random.randint(1,125), random.randint(1,125), random.randint(1,125))

    def draw(self, screen):
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.rayon)

    def move(self, screen_width, screen_height):
        self.x+= self.speed_x
        self.y += self.speed_y


        if (self.x+self.rayon)>=screen_width or (self.x)<=self.rayon:
            self.speed_x=-(self.speed_x)

        if (self.y+self.rayon)>=screen_height or (self.y)<=self.rayon:
            self.speed_y=-(self.speed_y)

import pygame
import random


SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72


pygame.init()


background_image = pygame.transform.scale(pygame.image.load("bg.jpj"),
                                          (SCREEN_WIDTH, SCREEN_HEIGHT))


font = pygame.font.Sysfont(Times New Roman", FONT_SIZE)
                           

class Sprite(pygame.sprite.Sprite):

    def __init__(self, colour, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Colour('dodgerblue'))
        pygame.draw.rect(self.image, colour, pygame.Rect(0, 0, width,
height))

   def move(self, x_change, y_change):
       self.rect.x = max(
           min(self.rect.x + x_change, SCREEN_WIDTH)
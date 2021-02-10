import pygame

class Window:
    def __init__(self):
        self.width = 700
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
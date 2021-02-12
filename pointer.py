import pygame
from window import Window

class Pointer(Window):
    def __init__(self):
        super().__init__()
        self.pos = (0, 0)
        self.column = 0

    def point_draw(self):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] < 100:
            self.column = 0
        elif self.pos[0] > 100 and self.pos[0] < 200:
            self.column = 1
        elif self.pos[0] > 200 and self.pos[0] < 300:
            self.column = 2
        elif self.pos[0] > 300 and self.pos[0] < 400:
            self.column = 3
        elif self.pos[0] > 400 and self.pos[0] < 500:
            self.column = 4
        elif self.pos[0] > 500 and self.pos[0] < 600:
            self.column = 5
        elif self.pos[0] > 600 and self.pos[0] < 700:
            self.column = 6
        
        self.draw_bg()
        pygame.draw.circle(self.screen, (255, 0, 0), (self.column * 100 + 50, 50), 45, width=0)
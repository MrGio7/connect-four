import pygame
from window import Window

class Pointer(Window):
    def __init__(self):
        super().__init__()
        self.pos = (0, 0)
        self.row = 0

    def point_draw(self):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] < 100:
            self.row = 0
        elif self.pos[0] > 100 and self.pos[0] < 200:
            self.row = 1
        elif self.pos[0] > 200 and self.pos[0] < 300:
            self.row = 2
        elif self.pos[0] > 300 and self.pos[0] < 400:
            self.row = 3
        elif self.pos[0] > 400 and self.pos[0] < 500:
            self.row = 4
        elif self.pos[0] > 500 and self.pos[0] < 600:
            self.row = 5
        elif self.pos[0] > 600 and self.pos[0] < 700:
            self.row = 6
        
        self.draw_bg()
        pygame.draw.circle(self.screen, (255, 0, 0), (self.row * 100 + 50, 50), 45, width=0)
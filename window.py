import pygame

class Window:
    def __init__(self):
        self.width = 700
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.rect = [0, 100, 700, 600]
        self.circle= []

    def draw_bg(self, bg_color, board_color):
        self.screen.fill(bg_color)
        pygame.draw.rect(self.screen, board_color, self.rect, width=0)

        cirx = -50
        for i in range(7):
            cirx += 100
            ciry = 50
            for i in range(6):
                ciry += 100
                self.circle.append([cirx, ciry])
        
        for i in self.circle:
            pygame.draw.circle(self.screen, (0, 0, 0), i, 45, width=0)
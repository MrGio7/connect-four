import pygame

class Window:
    def __init__(self):
        self.width = 700
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.rect = [0, 100, 700, 600]
        self.circle= []
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.CYAN = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PINK = (255, 0, 255)
        self.BLACK = (0, 0, 0)

    def draw_bg(self):
        self.screen.fill(self.BLACK)
        pygame.draw.rect(self.screen, self.BLUE, [0, 100, 700, 600], width=0)

        if len(self.circle) < 42:
            cirx = -50
            for i in range(7):
                cirx += 100
                ciry = 50
                for i in range(6):
                    ciry += 100
                    self.circle.append([cirx, ciry])
        
        for i in self.circle:
            pygame.draw.circle(self.screen, (0, 0, 0), i, 45, width=0)
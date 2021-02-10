import pygame
from window import Window

pygame.init()

window = Window()

#COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
BLACK = (0, 0, 0)

loop = True
while loop:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            loop = False
    
    pygame.display.set_caption("Connect Four By MrGio7")

    window.draw_bg(BLACK, BLUE)
    
    pygame.display.update()
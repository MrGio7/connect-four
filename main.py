import pygame
from pointer import Pointer

pygame.init()

pointer = Pointer()

loop = True
while loop:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            loop = False
    
    pygame.display.set_caption("Connect Four By MrGio7")

    pointer.point_draw()
    
    pygame.display.update()
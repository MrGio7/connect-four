import pygame
from gameplay import Gameplay

pygame.init()

gameplay = Gameplay()

loop = True
while loop:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            loop = False
    
    pygame.display.set_caption("Connect Four By MrGio7")

    gameplay.score_check()
    gameplay.gameplay()
    
    pygame.display.update()
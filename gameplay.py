from pointer import Pointer
import pygame
import numpy as np

class Gameplay(Pointer):
    def __init__(self):
        super().__init__()
        self.rows = 6
        self.columns = 7
        self.body = np.zeros((self.rows, self.columns))
        self.draw_id = -1
        self.response = 0
        self.turn = 1

    def gameplay(self):
        key = pygame.mouse.get_pressed()
        self.response += 1
        if key == (1, 0, 0) and self.response > 500:
            for r in range(self.rows):
                if self.body[r][self.column] == 0:
                    self.draw_id += 1
            if self.turn == 1:
                self.body[self.draw_id][self.column] = 1
                self.draw_id = -1
                self.response = 0
                self.turn = 2
            elif self.turn == 2:
                self.body[self.draw_id][self.column] = 2
                self.draw_id = -1
                self.response = 0
                self.turn = 1
            print(self.body)

        self.point_draw()
        for r in range(self.rows):
            for c in range(self.columns):
                posx = c * 100
                posy = r * 100
                if self.body[r][c] == 0:
                    pass
                elif self.body[r][c] == 1:
                    pygame.draw.circle(self.screen, self.RED, (posx + 50, posy + 150), 45, width=0)
                elif self.body[r][c] == 2:
                    pygame.draw.circle(self.screen, self.YELLOW, (posx + 50, posy + 150), 45, width=0)
                else:
                    pass
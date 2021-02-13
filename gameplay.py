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
        self.winner = 0

    def gameplay(self):
        if self.winner == 0:
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

    def score_check(self):
        for r in range(self.rows - 3):
            for c in range(self.columns):
                if self.body[r][c] == 1 and self.body[r + 1][c] == 1 and self.body[r + 2][c] == 1 and self.body[r + 3][c] == 1:
                    self.winner = 1
                
        for r in range(self.rows - 3):
            for c in range(self.columns):
                if self.body[r][c] == 2 and self.body[r + 1][c] == 2 and self.body[r + 2][c] == 2 and self.body[r + 3][c] == 2:
                    self.winner = 2    

        for r in range(self.rows):
            for c in range(self.columns - 3):
                if self.body[r][c] == 1 and self.body[r][c + 1] == 1 and self.body[r][c + 2] == 1 and self.body[r][c + 3] == 1:
                    self.winner = 1

        for r in range(self.rows):
            for c in range(self.columns - 3):
                if self.body[r][c] == 2 and self.body[r][c + 1] == 2 and self.body[r][c + 2] == 2 and self.body[r][c + 3] == 2:
                    self.winner = 2

        for r in range(self.rows - 3):
            for c in range(self.columns - 3):
                if self.body[r][c] == 1 and self.body[r + 1][c + 1] == 1 and self.body[r + 2][c + 2] == 1 and self.body[r + 3][c + 3] == 1:
                    self.winner = 1

        for r in range(self.rows - 3):
            for c in range(self.columns - 3):
                if self.body[r][c] == 2 and self.body[r + 1][c + 1] == 2 and self.body[r + 2][c + 2] == 2 and self.body[r + 3][c + 3] == 2:
                    self.winner = 2

        for r in range(self.rows - 3):
            for c in range(3, self.columns):
                if self.body[r][c] == 2 and self.body[r - 1][c + 1] == 2 and self.body[r - 2][c + 2] == 2 and self.body[r - 3][c + 3] == 2:
                    self.winner = 2

        for r in range(self.rows - 3):
            for c in range(3, self.columns):
                if self.body[r][c] == 1 and self.body[r - 1][c + 1] == 1 and self.body[r - 2][c + 2] == 1 and self.body[r - 3][c + 3] == 1:
                    self.winner = 1

        if self.winner == 0:
            pass
        elif self.winner == 1:
            font = pygame.font.SysFont(None, 75)
            text = font.render("Winner Player 1", True, self.RED)
            self.screen.blit(text, (150, 25))
        elif self.winner == 2:
            font = pygame.font.SysFont(None, 75)
            text = font.render("Winner Player 2", True, self.YELLOW)
            self.screen.blit(text, (150, 25))
import time
from random import sample

import pygame

from variables import diff_linker, numbers
from variables import width, height, coords


class Text():
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos

    def draw(self, window):
        window.blit(
            self.text,
            self.pos
        )


class Tile():
    def __init__(self, color, x, y, around):
        self.color = color
        self.x = x
        self.y = y
        self.hidden = True
        self.around = around
        self.locked = False

    def draw(self, window):
        pygame.draw.rect(
            surface=window,
            color=self.color,
            rect=pygame.Rect(self.x, self.y, 20, 20),
            border_radius=2,
        )


class Board():
    def __init__(self, diff, window):
        self.diff = diff
        self.squares = width * height // 400
        self.amount = round(self.squares * diff_linker[self.diff])
        self.grid = self.build_grid()
        self.found = 0
        self.objects = []
        self.window = window
        self.draw(self.window)

    def build_grid(self):
        bombs = sample(
            range(1, self.squares + 1),
            self.amount
        )

        grid = []
        counter = 1
        for row in range(height // 20):
            row = []

            for _ in range(width // 20):
                value = 0

                if counter in bombs:
                    value = 1

                counter += 1
                row.append(value)
            grid.append(row)

        return grid

    def draw(self, window):
        x, y = 0, 0
        window.fill((30, 30, 30))

        for row in self.grid:
            for _ in row:
                self.objects.append(
                    Tile(
                        color=(200, 200, 200),
                        x=x,
                        y=y,
                        around=self.get_surroundings(
                            x // 20, y // 20
                        )
                    )
                )
                x += 20
            y += 20
            x = 0

    def get_surroundings(self, x, y):
        count = 0

        for x2, y2 in coords:
            if 0 <= y + y2 < len(self.grid) and \
                    0 <= x + x2 < len(self.grid[0]) and \
                    self.grid[y + y2][x + x2]:
                count += 1

        return count


    def discover(self, x, y, chain=False):
        if not (0 <= y < len(self.grid) and 
                0 <= x < len(self.grid[0])) or (
                chain and self.grid[y][x]):
            return
             
        if not chain and self.grid[y][x]:
            font = pygame.font.SysFont('arial', 20)
            text = font.render(
                "X",
                True,
                (0, 0, 0)
            )
            self.objects.append(Text(text, (x * 20 + 5, y * 20 - 2)))
            self.game_over()
        else:
            index = x + y * width // 20
            index = self.objects[index]
            if not index.hidden or \
                    (index.locked):
                return

            self.found += 1
            index.color = (255, 105, 180)
            index.hidden = False

            if index.around:
                font = pygame.font.SysFont('arial', 20)
                text = font.render(
                    str(index.around),
                    True,
                    numbers[index.around]
                )
                self.objects.append(Text(text, (x * 20 + 5, y * 20 - 2)))
                return

            for x2, y2 in coords:
                self.discover(x + x2, y + y2, True)

    def check_win(self):
        if self.found == self.squares - self.amount:
            font = pygame.font.SysFont('arial', 50)
            text = font.render(
                "You win!",
                True,
                (0, 255, 0)
            )
            self.objects.append(Text(text, (width // 3, height // 2)))
            self.reset()

    def game_over(self):
        font = pygame.font.SysFont('arial', 50)
        text = font.render(
            "You lose",
            True,
            (0, 0, 0)
        )
        self.objects.append(Text(text, (width // 3, height // 2)))
        self.reset()

    def reset(self):
        for object_ in self.objects:
            object_.draw(self.window)
        pygame.display.update()
        time.sleep(3)

        self.grid = self.build_grid()
        self.found = 0
        self.objects = []
        self.draw(self.window)

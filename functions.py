from typing import List

import pygame

from variables import width
from classes import Text


def initialize(name: str, width: int, height: int) \
        -> pygame.display:
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)

    return window


def update(objects: List[object], window) -> None:
    for object_ in objects:
        object_.draw(window)

    pygame.display.update()


def handle_mouse(event, board):
    x, y = pygame.mouse.get_pos()
    x, y = x // 20, y // 20
    index = x + y * width // 20

    if event.button == 1 and not board.objects[index].locked:
        board.discover(x, y)
        board.check_win()
    elif event.button == 3:
        if board.objects[index].locked:
            board.objects[index].locked = False

            for object_ in board.objects[::-1]:
                if object_.pos == (x * 20 + 5, y * 20 - 2):
                    board.objects.remove(object_)
                    break
        else:
            if board.objects[index].hidden:
                board.objects[index].locked = True
                font = pygame.font.SysFont('arial', 20)
                text = font.render("P", True, (255, 0, 0))
                board.objects.append(
                    Text(
                        text=text,
                        pos=(x * 20 + 5, y * 20 - 2)
                    )
                )

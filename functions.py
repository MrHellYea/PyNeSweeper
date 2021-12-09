from typing import List

import pygame


def initialize(name: str, width: int, height: int) \
        -> pygame.display:
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)

    return window


def update(objects: List[object]) -> None:
    for object_ in objects:
        object_.draw()

    pygame.display.update()

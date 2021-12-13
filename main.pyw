import pygame

from classes import Board, Text
from variables import fps, width, difficulty
from variables import name, width, height
from functions import update, handle_mouse, initialize


def main():
    pygame.init()

    window = initialize(
        name=name,
        width=width,
        height=height
    )
    clock = pygame.time.Clock()
    board = Board(difficulty.lower(), window)

    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse(event, board)

        update(board.objects, window)
    pygame.quit()


if __name__ == "__main__":
    main()

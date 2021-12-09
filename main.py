import pygame

from classes import Board, Text
from variables import fps, width, difficulty
from functions import update


def main():
    pygame.init()

    clock = pygame.time.Clock()
    board = Board(difficulty.lower())

    run = True
    win = False
    while run:
        delta = clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
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

        update(board.objects)
    pygame.quit()


if __name__ == "__main__":
    main()

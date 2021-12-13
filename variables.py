closest = lambda x: max(200, round(x / 20) * 20)

name = "Minesweeper"
width = closest(60)
height = closest(60)
difficulty = "medium"  # easy, medium or hard

coords = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
)

fps = 60

diff_linker = {
    "easy": 0.05,
    "medium": 0.08,
    "hard": 0.12
}

numbers = {
    1: (0, 255, 0),
    2: (100, 255, 0),
    3: (200, 255, 0),
    4: (255, 255, 0),
    5: (0, 0, 255),
    6: (100, 100, 100),
    7: (40, 40, 40),
    8: (0, 0, 0)
}

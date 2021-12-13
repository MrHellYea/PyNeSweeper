name = "Minesweeper"
width = 400
height = 600
difficulty = "easy"  # easy, medium or hard

coords = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
)

fps = 60

diff_linker = {
    "easy": 0.05,
    "medium": 0.10,
    "hard": 0.15
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

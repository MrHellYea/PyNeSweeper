from functions import initialize


name = "Minesweeper"
width = 400
height = 600
difficulty = "easy"  # easy, medium or hard

window = initialize(
            name=name,
            width=width,
            height=height
        )

fps = 60

diff_linker = {
    "easy": 0.02,
    "medium": 0.05,
    "hard": 0.10
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

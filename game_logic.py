import random

class GameLogic:
    def __init__(self, color_grid):
        self.color_grid = color_grid
        self.target_coord = None

    def start_new_game(self):
        self.target_coord = (random.randint(0, self.color_grid.rows - 1),
                             random.randint(0, self.color_grid.cols - 1))
        return self.target_coord

    def get_actual_block_info(self):
        r, c = self.target_coord
        button = self.color_grid.blocks[(r, c)]
        color = button.cget("bg")
        return f"Actual Block - Color: {color}, Coordinates: ({r}, {c})"

    def check_win_condition(self, square_coords):
        sr, sc, er, ec = square_coords
        target_r, target_c = self.target_coord
        return (sr <= target_r <= er) and (sc <= target_c <= ec)

    def calculate_proximity(self, square_coords):
        sr, sc, er, ec = square_coords
        target_r, target_c = self.target_coord
        min_distance = float('inf')
        for r in range(sr, er + 1):
            for c in range(sc, ec + 1):
                distance = abs(target_r - r) + abs(target_c - c)
                min_distance = min(min_distance, distance)
        return min_distance

import tkinter as tk
import requests
import pandas as pd
from tkinter import simpledialog
from grid import ColorGrid
from game_logic import GameLogic
from utils import show_custom_message_box, collect_winner_details

class HuesAndCuesGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hues and Cues")

        # Main frame for layout
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill='both', expand=True)

        # Frame for the color grid
        self.grid_frame = tk.Frame(self.main_frame)
        self.grid_frame.pack(side='left', fill='both', expand=True)

        # Frame for the overlay canvas
        self.overlay_frame = tk.Frame(self.main_frame)
        self.overlay_frame.pack(side='left', fill='both', expand=True)
        self.overlay_frame.lift()  # Ensure overlay frame is on top

        # Canvas for the color grid
        self.color_grid_canvas = tk.Canvas(self.grid_frame, bg='white')
        self.color_grid_canvas.pack(fill='both', expand=True)

        # Canvas for overlay
        self.overlay_canvas = tk.Canvas(self.overlay_frame, bg='white', highlightthickness=0)
        self.overlay_canvas.pack(fill='both', expand=True)

        # Initialize color grid
        self.color_grid = ColorGrid(self.color_grid_canvas, rows=25, cols=40, on_block_click=self.handle_block_click)
        self.game_logic = GameLogic(self.color_grid)

        # Initialize the game
        self.target_coord = self.game_logic.start_new_game()
        self.target_color = self.color_grid.blocks[self.target_coord].cget("bg")
        print(f"Target Coordinate: {self.target_coord}, Target Color: {self.target_color}")

        # Send initial game data to Flask server
        self.send_data_to_flask(self.target_coord, self.target_color)

        # Frame for the right panel with buttons
        self.side_frame = tk.Frame(self.main_frame)
        self.side_frame.pack(side='right', fill='y', padx=10, pady=10)

        # Evaluate button
        self.evaluate_button = tk.Button(self.side_frame, text="Evaluate", command=self.evaluate_guess)
        self.evaluate_button.pack(pady=10)

        # Restart button
        self.restart_button = tk.Button(self.side_frame, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)

        # Initialize selected block
        self.selected_block = None

    def handle_block_click(self, row, col):
        # Handle block click events
        if self.selected_block:
            self.reset_sunk_blocks()
        self.selected_block = (row, col)
        self.sink_blocks(row, col)

    def sink_blocks(self, row, col):
        for r in range(max(0, row - 1), min(self.color_grid.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.color_grid.cols, col + 2)):
                self.color_grid.blocks[(r, c)].config(relief=tk.SUNKEN)

    def reset_sunk_blocks(self):
        for r in range(self.color_grid.rows):
            for c in range(self.color_grid.cols):
                self.color_grid.blocks[(r, c)].config(relief=tk.RAISED)

    def evaluate_guess(self):
        # Evaluate the guess and end the game
        self.end_game()

    def end_game(self):
        is_win = self.game_logic.check_win_condition(self.get_block_coords())
        actual_block_info = self.game_logic.get_actual_block_info()
        proximity = self.game_logic.calculate_proximity(self.get_block_coords())

        color = self.color_grid.blocks[self.target_coord].cget("bg")
        if is_win:
            result_msg = f"You won!\n\n{actual_block_info}\n"
            # Collect winner details when the game is won
            collect_winner_details(self.root)
        else:
            result_msg = f"You lost!\n\n{actual_block_info}\nProximity: {proximity}"
            show_custom_message_box(self.root, result_msg, self.restart_game, color)

        # Update Flask with the result
        self.send_data_to_flask(self.target_coord, color)

    def get_block_coords(self):
        # Return the coordinates of the selected block and its surrounding blocks
        if not self.selected_block:
            return (0, 0, 0, 0)  # Default if no block is selected

        row, col = self.selected_block
        sr, sc = max(0, row - 1), max(0, col - 1)
        er, ec = min(self.color_grid.rows - 1, row + 1), min(self.color_grid.cols - 1, col + 1)
        return (sr, sc, er, ec)

    def restart_game(self):
        # Restart the game
        self.color_grid.reset_grid()
        self.target_coord = self.game_logic.start_new_game()
        self.target_color = self.color_grid.blocks[self.target_coord].cget("bg")
        print(f"Target Coordinate: {self.target_coord}, Target Color: {self.target_color}")

        # Send updated game data to Flask server
        self.send_data_to_flask(self.target_coord, self.target_color)
        # Notify the Flask server to reload the webpage
        # try:
        #     requests.get('http://192.168.56.1:5000/reload')
        # except requests.RequestException as e:
        #     print(f"Failed to reload webpage: {e}")

        self.reset_sunk_blocks()
        self.selected_block = None
        

    def send_data_to_flask(self, coord, color):
        try:
            requests.post('http://192.168.56.1:5000/update', json={'coordinates': coord, 'color': color})
        except Exception as e:
            print(f"Error sending data to Flask: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HuesAndCuesGame(root)
    root.mainloop()

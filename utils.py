import tkinter as tk
from tkinter import simpledialog
import pandas as pd

def show_custom_message_box(root, message, on_restart, color):
    def restart_game():
        top.destroy()
        on_restart()

    top = tk.Toplevel(root)
    top.title("Game Over")

    # Calculate the position to center the window
    window_width = 300  # Adjust width as needed
    window_height = 200  # Adjust height as needed

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)

    top.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    label = tk.Label(top, text=message, padx=20, pady=20)
    label.pack()

    color_display = tk.Label(top, bg=color, width=20, height=2)
    color_display.pack(pady=10)

    restart_button = tk.Button(top, text="Restart", command=restart_game, padx=10, pady=5)
    restart_button.pack(pady=10)

    top.mainloop()


def collect_winner_details(root):
    def save_winner_details(p1_name, p1_insta, p1_number, p2_name, p2_insta, p2_number):
        try:
            df = pd.read_excel('winners.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Player1 Name', 'Player1 Entry', 'Player2 Name', 'Player2 Entry'])

        new_entry = pd.DataFrame([{
            'Player1 Name': p1_name,
            'Player1 Insta': p1_insta,
            'Player1 Number': p1_number,            
            'Player2 Name': p2_name,
            'Player2 Insta': p2_insta,
            'Player2 Number': p2_number
        }])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_excel('winners.xlsx', index=False)

    p1_name = simpledialog.askstring("You Won!", "Enter Player 1 Name:", parent=root)
    p1_insta = simpledialog.askstring("You Won!", "Enter Player 1 Insta Handle:", parent=root)
    p1_number = simpledialog.askstring("You Won!", "Enter Player 1 Number:", parent=root)
    p2_name = simpledialog.askstring("You Won!", "Enter Player 2 Name:", parent=root)
    p2_insta = simpledialog.askstring("You Won!", "Enter Player 2 Insta Handle:", parent=root)
    p2_number = simpledialog.askstring("You Won!", "Enter Player 2 Number:", parent=root)

    if p1_name and p1_insta and p2_name and p2_insta and p1_number and p2_number:
        save_winner_details(p1_name, p1_insta, p1_number, p2_name, p2_insta, p2_number)

import tkinter as tk
from tkinter import simpledialog
import pandas as pd

def show_custom_message_box(root, message, on_restart, color):
    def restart_game():
        top.destroy()
        on_restart()

    top = tk.Toplevel(root)
    top.title("Game Over")

    label = tk.Label(top, text=message, padx=20, pady=20)
    label.pack()

    color_display = tk.Label(top, bg=color, width=20, height=2)
    color_display.pack(pady=10)

    restart_button = tk.Button(top, text="Restart", command=restart_game, padx=10, pady=5)
    restart_button.pack(pady=10)

    top.mainloop()

def collect_winner_details(root):
    def save_winner_details(p1_name, p1_entry, p2_name, p2_entry):
        try:
            df = pd.read_excel('winners.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Player1 Name', 'Player1 Entry', 'Player2 Name', 'Player2 Entry'])

        new_entry = pd.DataFrame([{
            'Player1 Name': p1_name,
            'Player1 Entry': p1_entry,
            'Player2 Name': p2_name,
            'Player2 Entry': p2_entry
        }])

        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_excel('winners.xlsx', index=False)

    p1_name = simpledialog.askstring("Input", "Enter Player 1 Name:", parent=root)
    p1_entry = simpledialog.askstring("Input", "Enter Player 1 Entry Number:", parent=root)
    p2_name = simpledialog.askstring("Input", "Enter Player 2 Name:", parent=root)
    p2_entry = simpledialog.askstring("Input", "Enter Player 2 Entry Number:", parent=root)

    if p1_name and p1_entry and p2_name and p2_entry:
        save_winner_details(p1_name, p1_entry, p2_name, p2_entry)

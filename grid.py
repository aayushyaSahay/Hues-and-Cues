import tkinter as tk
import colorsys

class ColorGrid(tk.Frame):
    def __init__(self, parent, rows, cols, on_block_click):
        super().__init__(parent)
        self.rows = rows
        self.cols = cols
        self.on_block_click = on_block_click
        self.blocks = {}
        self.create_grid()
        self.pack(side='left', padx=10, pady=10)

    def create_grid(self):
        # Create column number labels
        for c in range(self.cols):
            label = tk.Label(self, text=str(c), width=2, borderwidth=1, relief="solid")
            label.grid(row=0, column=c + 1, padx=1, pady=1)
        
        # Create row number labels and grid buttons
        for r in range(self.rows):
            # Row number label
            label = tk.Label(self, text=str(r), width=2, borderwidth=1, relief="solid")
            label.grid(row=r + 1, column=0, padx=1, pady=1)
            
            for c in range(self.cols):
                hue = r / self.rows
                lightness = (c / self.cols) * 0.6 + 0.4  # Make colors shinier
                rgb = colorsys.hls_to_rgb(hue, 0.6, lightness)
                color = "#{:02x}{:02x}{:02x}".format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
                button = tk.Button(self, bg=color, width=2, height=1,
                                   command=lambda r=r, c=c: self.on_block_click(r, c))
                button.grid(row=r + 1, column=c + 1, padx=1, pady=1)
                self.blocks[(r, c)] = button

    def reset_grid(self):
        # Optionally implement reset functionality
        pass

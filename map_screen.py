import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Map_Screen(tk.Frame):
    def __init__(self,game):
        super().__init__(game.ventana)
        self.game = game
        self.build_ui()

    def build_ui(self):
        map_frame = tk.Frame(self)
        map_frame.pack(pady=10)

        map_label= tk.Label(map_frame, text="World Overview")
        map_label.pack()

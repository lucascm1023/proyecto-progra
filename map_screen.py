#importaciones de archivos
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#comportamiento de la ventana del mini mapa
class Map_Screen(tk.Frame):
    #constructor de la ventana
    def __init__(self,game):
        super().__init__(game.ventana)
        self.game = game
        self.build_ui()
    # metodo del user interface
    def build_ui(self):
        map_frame = tk.Frame(self)
        map_frame.pack(pady=10)

        #titulo de la ventana 
        map_label= tk.Label(map_frame, text="World Overview")
        map_label.pack()

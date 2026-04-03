import tkinter as tk
from game import Game

def main():
    ventana = tk.Tk()
    game= Game(ventana)
    ventana.mainloop()

if __name__== "__main__":
    main()

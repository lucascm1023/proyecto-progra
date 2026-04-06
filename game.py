#importaciones de archivos y de clases
import tkinter
import csv
from jugador import Jugador
from main_screen import Main_Screen
from map_screen import Map_Screen
from hollow import Hollow
from personaje import Personaje

#comportamiento de la clase game
class Game:
    #constructor de la ventana principal
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Juego Proyecto")
        self.ventana.geometry("1600x900")
        self.all_characters=[]
        self.starting_characters=[]
        self.player_name= ""
        self.player_avatar=""
        self.build_characters()
        self.current_screen=None
        self.change_screen(Main_Screen)
    # metodo para pasara a la ventana del mini mapa    
    def change_screen(self,screen_class):
        #se revisa que no haya otra ventana abierta antes de pasar de ventana
        if self.current_screen is not None:
            self.current_screen.destroy()

        self.current_screen = screen_class(self)
        self.current_screen.pack(fill="both",expand=True)

    #metodo de la construccion de los personajes con un archivo de texto
    def build_characters(self):
        #se convierten los datos en listas y cada fila es una lista
        with open("characters.txt", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for fila in reader:
                character = Personaje(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.all_characters.append(character)
    #metodo para inicializar el juego       
    def initialize_game(self):
        self.player = Jugador(self.player_name,self.player_avatar,self.starting_characters)
        self.hollow1 = Hollow("Hollow 1","hollow1.png",self.all_characters)
        self.hollow2 = Hollow("Hollow 2","hollow2.jpg",self.all_characters)
        self.hollow3 = Hollow("Hollow 3","hollow3.jpg",self.all_characters)
        self.hollow4 = Hollow("Hollow 4","hollow4.png",self.all_characters)
        self.hollow5 = Hollow("Hollow 5","hollow5.jpg",self.all_characters)

        self.change_screen(Map_Screen)

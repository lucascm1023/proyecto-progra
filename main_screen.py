#importaciones de archivos 
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#comportamiento de la pantalla principal
class Main_Screen(tk.Frame):
    #constructor de la clase
    def __init__(self, game):
        super().__init__(game.ventana)
        self.game = game
        self.player_name_var = tk.StringVar()
        self.photo_references=[]
        self.selection_data=[]
        self.avatar1_path = "avatar1.png"
        self.avatar2_path = "avatar2.jpg"
        self.avatar3_path = "avatar3.jpg"
        self.all_characters = game.all_characters
        self.selected_avatar = tk.StringVar(value= "none")
        
        self.build_ui()

    # metodo para empezar el juego
    def start_game(self):
        player_name = self.player_name_var.get()
        player_avatar = self.selected_avatar.get()
        selected_characters=[]
        #se revisa si el personaje fue seleccionado
        for pair in self.selection_data:
            character= pair[0]
            selected= pair[1]
            if selected.get()== True:
                selected_characters.append(character)
        #se revisa que los personajes seleccionados sean solo 3        
        if len(selected_characters)!=3:
            messagebox.showwarning("Invalid character selection", "You must select exactly 3 characters")
            return
        #se revisa que el jugador ingrese su nombre
        if player_name == "":
            messagebox.showwarning("Invalid name", "You must enter a name")
            return
        #se revisa que el jugador haya seleccionado un avatar
        if player_avatar == "none":
            messagebox.showwarning("Invalid avatar selection", "You must select exactly 1 avatar")
            return
        self.game.starting_characters= selected_characters
        self.game.player_name=player_name
        self.game.player_avatar= player_avatar
        
        print(player_name)
        print(player_avatar)
        print("Current characters:")
        #muestra el nombre del personaje seleccionado 
        for character in self.game.starting_characters:
            print(character.name)
            
        self.game.initialize_game()

    #metodo de la creacion de los personajes en la ventana
    def build_character_list(self):
        choose_character_frame= tk.Frame(self)
        choose_character_frame.pack()
        character_grid_frame = tk.Frame(self)
        character_grid_frame.pack(pady=10)
        choose_character_label= tk.Label(choose_character_frame, text= "Choose 3 Characters")
        choose_character_label.pack()
        row=0
        column=0
        #revisa que cuando haya 5 personajes en una columna, el siguiente personaje ira en la siguiente fila
        for character in self.all_characters:
            character_frame = tk.Frame(character_grid_frame)
            character_frame.grid(row= row, column=column)
            column= column+1
            if column == 5:
                column=0
                row= row+1
            #crea los avatares de los personajes
            character_image = Image.open(character.avatar)
            character_image = character_image.resize((100,100))
            character_photo = ImageTk.PhotoImage(character_image)
            self.photo_references.append(character_photo)
            character_label = tk.Label(character_frame,image=character_photo)
            character_label.pack()

            #crea una lista de tuplas donde vaya (personaje, si esta seleccionado o no)
            selected=tk.BooleanVar()
            character_check = tk.Checkbutton(character_frame,text=character.name,variable=selected)
            character_check.pack()
            self.selection_data.append([character,selected])
            
    #metodo de la creacion del user interface    
    def build_ui(self):
        #titulo del juego
        tittle_label= tk.Label(self, text="Disney´s Epic Adventure", font=("Arial",18,"bold"))
        tittle_label.pack()
        
        name_frame = tk.Frame(self)
        name_frame.pack(pady=10)
        #etiqueta mostrandole al jugador donde ingresar el nombre
        name_label= tk.Label(name_frame, text="Enter your name:")
        name_label.pack()

        #barra de texto donde el jugador ingresa su nombre
        name_entry= tk.Entry(name_frame, textvariable=self.player_name_var, width=25)
        name_entry.pack()
        
        #colocacion de los avatares disponibles para la eleccion del jugador
        avatar_label_frame= tk.Frame(self)
        avatar_label_frame.pack()
        avatar_label= tk.Label(avatar_label_frame, text= "Choose your Avatar")
        avatar_label.pack()
        
        #grid para colocar los avatares
        avatar_grid_frame = tk.Frame(self)
        avatar_grid_frame.pack(pady=10)

        #crea el avatar 1 y lo acomoda en la ventana
        avatar1_frame = tk.Frame(avatar_grid_frame)
        avatar1_frame.grid(row=0,column=0)
        avatar1 = Image.open(self.avatar1_path)
        avatar1 = avatar1.resize((100,100))
        avatar1_photo = ImageTk.PhotoImage(avatar1)
        self.photo_references.append(avatar1_photo)
        avatar1_label = tk.Label(avatar1_frame, image=avatar1_photo)
        avatar1_label.pack()

        #boton para seleccionar el avatar 1
        avatar1_radio = tk.Radiobutton(avatar1_frame,text= "Select", variable= self.selected_avatar,value= self.avatar1_path)
        avatar1_radio.pack()

        #crea el avatar 2 y lo acomoda en la ventana
        avatar2_frame = tk.Frame(avatar_grid_frame)
        avatar2_frame.grid(row=0,column=1)
        avatar2 = Image.open(self.avatar2_path)
        avatar2 = avatar2.resize((100,100))
        avatar2_photo = ImageTk.PhotoImage(avatar2)
        self.photo_references.append(avatar2_photo)
        avatar2_label = tk.Label(avatar2_frame, image=avatar2_photo)
        avatar2_label.pack()

        #boton para seleccionar el avatar 2
        avatar2_radio = tk.Radiobutton(avatar2_frame,text= "Select", variable= self.selected_avatar,value= self.avatar2_path)
        avatar2_radio.pack()

        #crea el avatar 3 y lo acomoda en la ventana
        avatar3_frame = tk.Frame(avatar_grid_frame)
        avatar3_frame.grid(row=0,column=2)
        avatar3 = Image.open(self.avatar3_path)
        avatar3 = avatar3.resize((100,100))
        avatar3_photo = ImageTk.PhotoImage(avatar3)
        self.photo_references.append(avatar3_photo)
        avatar3_label = tk.Label(avatar3_frame, image=avatar3_photo)
        avatar3_label.pack()

        #boton para seleccionar el avatar 3
        avatar3_radio = tk.Radiobutton(avatar3_frame,text= "Select", variable= self.selected_avatar,value= self.avatar3_path)
        avatar3_radio.pack()
        #este tipo de boton solo permite seleccionar un avatar
        
        self.build_character_list()
    
        button_frame = tk.Frame(self)
        button_frame.pack()

        #boton para empezar el juego 
        start_button = tk.Button(button_frame,text= "Start Game", command= self.start_game)
        start_button.pack()

import tkinter as tk
from PIL import Image, ImageTk

class Main_Screen(tk.Frame):
    def __init__(self, game):
        super().__init__(game.ventana)
        self.game = game
        self.player_name_var = tk.StringVar()
        self.photo_references=[]
        self.avatar1_path = "avatar1.png"
        self.avatar2_path = "avatar2.jpg"
        self.avatar3_path = "avatar3.jpg"
        self.character1_path = "aladin.png"
        self.character2_path = "blanca_nieves.jpg"
        self.character3_path = "chewbacca.png"
        self.character4_path = "darth_vader.png"
        self.character5_path = "elsa.png"
        self.character6_path = "goofy.png"
        self.character7_path = "jessie.png"
        self.character8_path = "mickey.png"
        self.character9_path = "mulan.png"
        self.character10_path = "peter_pan.jpg"
        self.character11_path = "pinocho.jpg"
        self.character12_path = "pluto.jpg"
        self.character13_path = "stitch.png"
        self.character14_path = "winnie_pooh.png"
        self.character15_path = "woody.png"
        self.selected_avatar = tk.StringVar(value= "none")
        
        self.build_ui()

    def start_game(self):
        player_name = self.player_name_var.get()
        player_avatar = self.selected_avatar.get()
        if player_name == "":
            print("Enter your name")
            return
        if player_avatar == "none":
            print("Choose an avatar")
            return
        print(player_name)
        print(player_avatar)

    def build_character_list(self):
        
        character_grid_frame = tk.Frame(self)
        character_grid_frame.pack(pady=10)

        character1_frame = tk.Frame(character_grid_frame)
        character1_frame.grid(row= 0, column=0)
        character1 = Image.open(self.character1_path)
        character1 = character1.resize((100,100))
        character1_photo = ImageTk.PhotoImage(character1)
        self.photo_references.append(character1_photo)
        character1_label = tk.Label(character1_frame,image=character1_photo)
        character1_label.pack()

        character2_frame = tk.Frame(character_grid_frame)
        character2_frame.grid(row= 0, column=1)
        character2 = Image.open(self.character2_path)
        character2 = character2.resize((100,100))
        character2_photo = ImageTk.PhotoImage(character2)
        self.photo_references.append(character2_photo)
        character2_label = tk.Label(character2_frame,image=character2_photo)
        character2_label.pack()

        character3_frame = tk.Frame(character_grid_frame)
        character3_frame.grid(row= 0, column=2)
        character3 = Image.open(self.character3_path)
        character3 = character3.resize((100,100))
        character3_photo = ImageTk.PhotoImage(character3)
        self.photo_references.append(character3_photo)
        character3_label = tk.Label(character3_frame,image=character3_photo)
        character3_label.pack()

        character4_frame = tk.Frame(character_grid_frame)
        character4_frame.grid(row= 0, column=3)
        character4 = Image.open(self.character4_path)
        character4 = character4.resize((100,100))
        character4_photo = ImageTk.PhotoImage(character4)
        self.photo_references.append(character4_photo)
        character4_label = tk.Label(character4_frame,image=character4_photo)
        character4_label.pack()

        character5_frame = tk.Frame(character_grid_frame)
        character5_frame.grid(row= 0, column=4)
        character5 = Image.open(self.character5_path)
        character5 = character5.resize((100,100))
        character5_photo = ImageTk.PhotoImage(character5)
        self.photo_references.append(character5_photo)
        character5_label = tk.Label(character5_frame,image=character5_photo)
        character5_label.pack()

        character6_frame = tk.Frame(character_grid_frame)
        character6_frame.grid(row= 1, column=0)
        character6 = Image.open(self.character6_path)
        character6 = character6.resize((100,100))
        character6_photo = ImageTk.PhotoImage(character6)
        self.photo_references.append(character6_photo)
        character6_label = tk.Label(character6_frame,image=character6_photo)
        character6_label.pack()

        character7_frame = tk.Frame(character_grid_frame)
        character7_frame.grid(row= 1, column=1)
        character7 = Image.open(self.character7_path)
        character7 = character7.resize((100,100))
        character7_photo = ImageTk.PhotoImage(character7)
        self.photo_references.append(character7_photo)
        character7_label = tk.Label(character7_frame,image=character7_photo)
        character7_label.pack()

        character8_frame = tk.Frame(character_grid_frame)
        character8_frame.grid(row= 1, column=2)
        character8 = Image.open(self.character8_path)
        character8 = character8.resize((100,100))
        character8_photo = ImageTk.PhotoImage(character8)
        self.photo_references.append(character8_photo)
        character8_label = tk.Label(character8_frame,image=character8_photo)
        character8_label.pack()

        character9_frame = tk.Frame(character_grid_frame)
        character9_frame.grid(row= 1, column=3)
        character9 = Image.open(self.character9_path)
        character9 = character9.resize((100,100))
        character9_photo = ImageTk.PhotoImage(character9)
        self.photo_references.append(character9_photo)
        character9_label = tk.Label(character9_frame,image=character9_photo)
        character9_label.pack()

        character10_frame = tk.Frame(character_grid_frame)
        character10_frame.grid(row= 1, column=4)
        character10 = Image.open(self.character10_path)
        character10 = character10.resize((100,100))
        character10_photo = ImageTk.PhotoImage(character10)
        self.photo_references.append(character10_photo)
        character10_label = tk.Label(character10_frame,image=character10_photo)
        character10_label.pack()

        character11_frame = tk.Frame(character_grid_frame)
        character11_frame.grid(row= 2, column=0)
        character11 = Image.open(self.character11_path)
        character11 = character11.resize((100,100))
        character11_photo = ImageTk.PhotoImage(character11)
        self.photo_references.append(character11_photo)
        character11_label = tk.Label(character11_frame,image=character11_photo)
        character11_label.pack()

        character12_frame = tk.Frame(character_grid_frame)
        character12_frame.grid(row= 2, column=1)
        character12 = Image.open(self.character12_path)
        character12 = character12.resize((100,100))
        character12_photo = ImageTk.PhotoImage(character12)
        self.photo_references.append(character12_photo)
        character12_label = tk.Label(character12_frame,image=character12_photo)
        character12_label.pack()

        character13_frame = tk.Frame(character_grid_frame)
        character13_frame.grid(row= 2, column=2)
        character13 = Image.open(self.character13_path)
        character13 = character13.resize((100,100))
        character13_photo = ImageTk.PhotoImage(character13)
        self.photo_references.append(character13_photo)
        character13_label = tk.Label(character13_frame,image=character13_photo)
        character13_label.pack()

        character14_frame = tk.Frame(character_grid_frame)
        character14_frame.grid(row= 2, column=3)
        character14 = Image.open(self.character14_path)
        character14 = character14.resize((100,100))
        character14_photo = ImageTk.PhotoImage(character14)
        self.photo_references.append(character14_photo)
        character14_label = tk.Label(character14_frame,image=character14_photo)
        character14_label.pack()

        character15_frame = tk.Frame(character_grid_frame)
        character15_frame.grid(row= 2, column=4)
        character15 = Image.open(self.character15_path)
        character15 = character15.resize((100,100))
        character15_photo = ImageTk.PhotoImage(character15)
        self.photo_references.append(character15_photo)
        character15_label = tk.Label(character15_frame,image=character15_photo)
        character15_label.pack()
        
    def build_ui(self):
        tittle_label= tk.Label(self, text="Disney´s Epic Adventure", font=("Arial",18,"bold"))
        tittle_label.pack()

        name_frame = tk.Frame(self)
        name_frame.pack(pady=10)

        name_label= tk.Label(name_frame, text="Enter your name:")
        name_label.pack()

        name_entry= tk.Entry(name_frame, textvariable=self.player_name_var, width=25)
        name_entry.pack()

        avatar_grid_frame = tk.Frame(self)
        avatar_grid_frame.pack(pady=10)

        avatar1_frame = tk.Frame(avatar_grid_frame)
        avatar1_frame.grid(row=0,column=0)
        avatar1 = Image.open(self.avatar1_path)
        avatar1 = avatar1.resize((100,100))
        avatar1_photo = ImageTk.PhotoImage(avatar1)
        self.photo_references.append(avatar1_photo)
        avatar1_label = tk.Label(avatar1_frame, image=avatar1_photo)
        avatar1_label.pack()

        avatar1_radio = tk.Radiobutton(avatar1_frame,text= "Select", variable= self.selected_avatar,value= self.avatar1_path)
        avatar1_radio.pack()

        avatar2_frame = tk.Frame(avatar_grid_frame)
        avatar2_frame.grid(row=0,column=1)
        avatar2 = Image.open(self.avatar2_path)
        avatar2 = avatar2.resize((100,100))
        avatar2_photo = ImageTk.PhotoImage(avatar2)
        self.photo_references.append(avatar2_photo)
        avatar2_label = tk.Label(avatar2_frame, image=avatar2_photo)
        avatar2_label.pack()

        avatar2_radio = tk.Radiobutton(avatar2_frame,text= "Select", variable= self.selected_avatar,value= self.avatar2_path)
        avatar2_radio.pack()
        
        avatar3_frame = tk.Frame(avatar_grid_frame)
        avatar3_frame.grid(row=0,column=2)
        avatar3 = Image.open(self.avatar3_path)
        avatar3 = avatar3.resize((100,100))
        avatar3_photo = ImageTk.PhotoImage(avatar3)
        self.photo_references.append(avatar3_photo)
        avatar3_label = tk.Label(avatar3_frame, image=avatar3_photo)
        avatar3_label.pack()

        avatar3_radio = tk.Radiobutton(avatar3_frame,text= "Select", variable= self.selected_avatar,value= self.avatar3_path)
        avatar3_radio.pack()

        self.build_character_list()

        button_frame = tk.Frame(self)
        button_frame.pack()

        start_button = tk.Button(button_frame,text= "Start Game", command= self.start_game)
        start_button.pack()

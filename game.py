import tkinter
from main_screen import Main_Screen

from personaje import Personaje

mickey= Personaje(100,35,50,"mickey",None,None)
pluto= Personaje(100,45,50,"pluto",None,None)
winniepooh= Personaje(100,23,60,"winnie pooh",None,None)
goofy= Personaje(100,56,30,"goofy",None,None)
woody= Personaje(100,73,20,"woody",None,None)
stitch= Personaje(100,45,60,"stitch",None,None)
aladin= Personaje(100,60,49,"aladin",None,None)
elsa= Personaje(100,32,64,"elsa",None,None)
jessie= Personaje(100,67,40,"jessie",None,None)
peterpan= Personaje(100,37,68,"peter pan",None,None)
pinocho= Personaje(100,45,39,"pincho",None,None)
blancanieves= Personaje(100,40,50,"blancanieves",None,None)
mulan= Personaje(100,53,62,"mulan",None,None)
chewbaca= Personaje(100,55,70,"chewbaca",None,None)
darthvader= Personaje(100,88,34,"darth vader",None,None)

available_characters= [mickey,pluto,winniepooh,goofy,woody,stitch,aladin,elsa,jessie,peterpan,pinocho,blancanieves,mulan,chewbaca,darthvader]

class Game:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Juego Proyecto")
        self.ventana.geometry("700x600")
        self.current_screen=None
        self.change_screen(Main_Screen)

    def change_screen(self,screen_class):
        if self.current_screen is not None:
            self.current_screen.destroy()

        self.current_screen = screen_class(self)
        self.current_screen.pack(fill="both",expand=True)



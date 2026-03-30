"""
importacion de funcion random para el comportamiento del hollow
"""

import random

"""
Comportamiento y los datos que va a tener cada hollow
"""

class Hollow
selected_characters=[]
all_characters=[]
avatar= None
name= None
selected_character= None

    """
    metodo del constructor de la clase

    Le da los valores de avatar, name, y all_characters para que despues escoga los starting_characters
    """
    def __init__(self,avatar,name,all_characters):
        self.avatar= avatar
        self.name= name
        self.all_characters= all_characters
        choose_starting_characters()

    """
    Metodo de escoger los personajes iniciales de cada hollow

    random.sample(self.all_characters, 3) se utiliza para escoger 3 personajes al azar
    """

    def choose_starting_characters(self):
        self.selected_characters= random.sample(self.all_characters, 3)

    """
    Metodo de escoger el personaje para pelear

    se define una lista llamada alive_characters para luego añadirle los personajes que estan vivos

    luego se revisa que alive_characters no este vacia para seleccionar el personaje para la batalla
    """

    def choose_character(self):
        alive_characters=[]
        for character in self.selected_characters:
            if not character.Is_dead():
                alive_characters.append(character)
                
        if len(alive_characters)==0:
            selected_character=None
            return None
        else:
            selected_character= random.choice(alive_characters)
            return selected_character

    """
    Metodo de iniciar la batalla

    se le ordena a al selected_character que ataque al target
    """
    def set_battle_action(self, target):
        self.selected_character.Attack(target)

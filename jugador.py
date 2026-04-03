"""
comportamiento y datos del Jugador
"""
class Jugador:
    name= None
    avatar= None
    current_characters=[]
    all_characters=[]
    selected_character=None

    """
    metodo constructor de la clase

    Le da los valores de name, avatar y all_characters al Jugador
    """
    def __init__(self,name,avatar,all_characters):
        self.name= name
        self.avatar= avatar
        self.current_characters=[]


    """
    metodo de añadir los personajes iniciales

    se revisa si el character escogido esta en current_characters y si lo esta se muestra un mensaje de advertencia
    sino entonces se agrega el character seleccionado a current_characters
    """
    def add_starting_character(self,character):
        if character in self.current_characters:
            return print("Warning: Este personaje ya ha sido elegido, elija otro")
        
        else:
            self.current_characters.append(character)

            if len(current_characters) == 3:
                return True
            else:
                return False

    def add_character(self,character):
        self.current_characters.append(character)


    """
    metodo de escoger un character de los 3 disponibles

    se revisa que el character escogido este vivo y se agrega a una lista, si la longitud de esa lista es =0 entonces se retorna None
    sino se retorna el character seleccionado
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
                if not (0 <= character < len(alive_characters)):
                    raise IndexError(f"Índice {character} fuera de rango.")
            
            self.selected_character = alive_characters[character]
            return self.selected_character


    """
    metodo de iniciar la batalla
    se le ordena a al selected_character que ataque al target
    """
    def attack_action(self, target):
            self.selected_character.Attack(target)

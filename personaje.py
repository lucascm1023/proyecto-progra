"""
Clase personaje

Representacion de los personajes que puede usar el jugador y los hollows
"""
class Personaje:
    hp=0
    attack_value=0
    defense_value=0
    name=""
    avatar=None
    owner=None
    
    """
    metodo de la accion atacar

    restriccion: si el valor del target.defense_value es mayor o igual al valor del self.attack_value entonces el daño realizado es 1 (valor minimo)

    Sino entonces el daño se calcula con la resta del self.attack_value - target.defense_value

    La vida del target es igual a la resta de target.hp - damage
    """
    def Attack(self,target):
        if target.defense_value>= self.attack_value:
            damage=1
        else:
            damage= self.attack_value - target.defense_value
        target.hp -= damage

    """
    metodo para verificar si el personaje muere

    Si self.hp menor o igual a 0 entonces el personaje muere

    Sino el personaje sigue vivo
    """

    def Is_dead(self):
        if self.hp<=0:
            return True

        else:
            return False

    """
    metodo del constructor de la clase

    Le da los valores de hp, attack, defense, name, avatar y owner a cada personaje
    """

    def __init__(self,hp,attack,defense,name,avatar,owner):
        self.hp= hp
        self.attack_value= attack
        self.defense_value= defense
        self.name= name
        self.avatar= avatar
        self.owner= owner

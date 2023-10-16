"""
dans ce fichier se trouve la classe pokemon ou sont stocker les donner de chaque pokemoon tel
que leurs pv ou leurs type, et la definition fight 
"""
from efficacity import efficacite, feu, plante, eau
from attaque import attaque

class Pokemoon :
    def __init__(self, n: str, pv: int, type_feu: bool, type_eau: bool, type_plante: bool) -> None:
        self.nom = n
        self.pv = pv 
        self.alive = True
        self.p = 2 
        self.sp = 1
        self.type = type_feu, type_eau, type_plante
        self.type_feu = type_feu
        self.type_eau = type_eau
        self.type_plante = type_plante

    def fight(self, other):
        "cette definition permet de choisir ce que l'on veut faire pendant notre tour"
        input(f"Au tour de {self.nom}")
        action = int(input("coup d'boule(1) , attaque spéciale(2) , sac(3)  "))
        while action <= 0 or action >= 5:
            action = int(input("coup d'boule(1) , attaque spéciale(2) , sac(3)  "))
        if action == 1 :
            other.pv -=8
            print(f"{other.pv} (-8)")
        if action == 2 :
            if efficacite[(self.type,other.type)]:
                other.pv -= 30
                print("super efficace")
                print(f"{other.pv} (-30)")
            else :
                    other.pv -= 20
                    print(f"{other.pv} (-20)")
        if action == 3 :
            potions = int(input("potion(1) , super potion(2)  "))
            while potions <= 0 or potions >= 3:
                 potions = int(input("potion(1) , super potion(2)  "))
            if potions == 1 : 
                    if self.p >= 1 :
                        self.pv += 6
                        s = 6
                        self.p -= 1 
                        print(f"{self.nom}, {self.pv} (+{s})")
                    else : 
                        print("vous n'avez plus de potions")
            if potions == 2 : 
                    if self.sp >= 1:
                        self.pv += 10
                        s = 10
                        self.sp -= 1
                        print(f"{self.nom}, {self.pv} (+{s})")
                    else :
                        print("vous n'avez plus de super potions")
        if other.pv <= 0 :
            other.alive = False
import json
from efficacity import efficacite, feu, eau, plante 

class Pokémoon :
    def __init__(self, n: str, pv: int, type_feu: bool, type_eau: bool, type_plante: bool) -> None:
        self.nom = n
        self.pv = pv # nombre de pv du pokémon
        self.alive = True # True si tj en vie et inversement 
        self.p = 2 # potions
        self.sp = 1
        self.type = type_feu, type_eau, type_plante
        self.type_feu = type_feu
        self.type_eau = type_eau
        self.type_plante = type_plante

    def fight(self, other):
        input(f"Au tour de {self.nom}")
        action = int(input("coup d'boule(1) , charge(2) , sac(3)  "))# attaque spécifique au type(2)
        if action == 1 :
            other.pv -=8
        if action == 2 :
            if efficacite[(self.type,other.type)]:
                other.pv -= 30
                print("super efficace")
            else :
                    other.pv -= 20
        if action == 3 :
            soins = int(input("potion(1) , super potion(2)  "))# ça s'apelle tj soins mais c'est les potions 
            if soins == 1 : 
                    if self.p >= 1 :
                        self.pv += 6
                        s = 6
                        self.p -= 1 # nombre limiter de potion 
                        print(f"{self.nom}, {self.pv} (+{s})")
                    else : 
                        print("vous n'avez plus de potions")
            if soins == 2 : 
                    if self.sp >= 1:
                        self.pv += 10
                        s = 10
                        self.sp -= 1
                        print(f"{self.nom}, {self.pv} (+{s})")
                    else :
                        print("vous n'avez plus de super potions")
        if other.pv <= 0 :
            other.alive = False
               
class Jeu :

    def __init__(self,c1: Pokémoon,c2: Pokémoon):
        self.c1 = c1
        self.c2 = c2

    def run(self): #code du combat
        while self.c1.alive and self.c2.alive :
            x = self.c1
            y = self.c2
            while self.c1.alive and self.c2.alive >= 1:
                x.fight(y)
                x, y = y, x
            if not self.c1.alive :
                 print(f'{self.c2.nom} gagne')
            else : 
                 print(f'{self.c1.nom} gagne')

poke = [
    {"nom" : "salamèche", "pv" : 30, "type_feu": True, "type_eau": False, "type_plante": False},
    {"nom" : "darumarrond", "pv" : 30, "type_feu": True, "type_eau": False, "type_plante": False}
]
choix_perso = int(input("0"))
perso1 = poke[choix_perso]

def dic2poke(dic):
     return Pokémoon(dic["nom"], dic["pv"], dic["type_feu"], dic["type_eau"], dic["type_plante"])


c1 = Pokémoon("salameche", 30, True, False, False)
c2 = Pokémoon("salameche", 30, True, False, False)

j= Jeu(dic2poke(perso1),c2) #choix du pokémoon

j.run()

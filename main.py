"""
fichier pricipal du jeu ou se deroule les actions
"""
from pokemoon import Pokemoon
from choix_poke import choix_perso1
from choix_poke import choix_perso2 

class Jeu :

    def __init__(self,p1: Pokemoon,p2: Pokemoon):
        self.p1 = p1
        self.p2 = p2

    def run(self):
        "code du combat "
        while self.p1.alive and self.p2.alive:
            x = self.p1
            y = self.p2
            while self.p1.alive and self.p2.alive :
                x.fight(y)
                x, y = y, x
            if not self.p1.alive :
                 print(f'{self.p2.nom} gagne')
            else : 
                 print(f'{self.p1.nom} gagne')

j= Jeu(choix_perso(),choix_perso()) 

j.run()

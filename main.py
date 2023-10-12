from pokemoon_v5 import Pokémoon
class Jeu :

    def __init__(self,c1: Pokémoon,c2: Pokémoon):
        self.c1 = c1
        self.c2 = c2

    def run(self): #code du combat
        while self.c1.alive and self.c2.alive:
            x = self.c1
            y = self.c2
            while self.c1.alive and self.c2.alive :
                x.fight(y)
                x, y = y, x
            if not self.c1.alive :
                 print(f'{self.c2.nom} gagne')
            else : 
                 print(f'{self.c1.nom} gagne')

j= Jeu(c6,c3) #choix du pokémoon

j.run()
from pokemoon import Pokemoon

def attaque():
    action = int(input("attaque, sac"))
    while action <= 0 or action >= 3 :
        action = int(input("attaque, sac"))
    if action == 1 :
        if Pokemoon["type_feu"] == True :
            att = int(input("charge, flamèche"))
        if Pokemoon["type_eau"] == True :
            att = int(input("charge, bulle d'eau"))
        if Pokemoon["type_plante"] == True :
            att = int(input("charge, flamèche"))
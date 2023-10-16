"""
Dans ce fichier sont stocker les différentes fonction permettant de choisir son pokemoon
"""
from pokemoon import Pokemoon
import json

def get_data_poke(i):
    """
    lis dans le fichier data.json les dic correspondant a des pokemoon et renvoie celui choisis
    """
    with open("data.json", 'r') as file :
        poke = json.load(file)
    perso1 = poke[i]
    return perso1

def dic2poke(dic):
    "transforme le dic en pokemoon"
    return Pokemoon(dic["nom"], dic["pv"], dic["type_feu"], dic["type_eau"], dic["type_plante"])

def choix_perso1():
    "Déf permettant grace a un input de choisir son pokemoon pour le j1"
    choix_perso = int(input("salameche, darrumarond, carapuce, moustillon, bulbizzare, vipelierre "))
    while choix_perso <= 0 or choix_perso >= 7 :
        choix_perso = int(input("salameche, darrumarond, carapuce, moustillon, bulbizzare, vipelierre "))
    choix_perso -= 1
    p1 = dic2poke(get_data_poke(choix_perso))
    return p1

def choix_perso2():
    "Déf permettant grace a un input de choisir son pokemoon pour le j2"
    choix_perso = int(input("salameche, darrumarond, carapuce, moustillon, bulbizzare, vipelierre "))
    while choix_perso <= 0 or choix_perso >= 7 :
        choix_perso = int(input("salameche, darrumarond, carapuce, moustillon, bulbizzare, vipelierre "))
    choix_perso -= 1
    p2 = dic2poke(get_data_poke(choix_perso))
    return p2
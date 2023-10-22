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

def choix_perso():
    "Déf permettant grace a un input de choisir son pokemoon pour le j1"
    choix_p = int(input("salameche, darrumarond, carapuce, moustillon, bulbizzare, vipelierre "))
    while choix_p <= 0 or choix_p >= 7 :
        choix_p = int(input("salameche, darrumarond, carapuce, moustillon, bulbizzare, vipelierre "))
    choix_p -= 1
    p = dic2poke(get_data_poke(choix_p))
    return p
"""
dans ce fichier sont stoker les donnés des attaques super efficaces en fonction
du type du pokemoon, qui renvoi true si efficacite et false si l'inverse
"""
feu = True, False, False
eau = False, True, False
plante = False, False, True
efficacite = {
        (feu , plante) : True, 
        (feu , eau) : False,
        (feu , feu) : False,
        (plante , plante) : False,
        (plante , eau) : True,
        (plante , feu) : False,
        (eau , plante) : False,
        (eau , eau) : False,
        (eau , feu) : True
        }
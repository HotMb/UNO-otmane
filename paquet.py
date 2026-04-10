from carte import Carte
import random

class Paquet:

    def __init__(self):
        self.cartes = []
        for couleur in Carte.couleurs:
            for valeur in Carte.valeurs:
                self.cartes.append(Carte(valeur, couleur))

    def __len__(self):
        return len(self.cartes)
    
    def melanger(self):
        random.shuffle(self.cartes)
        return
    
    def __repr__(self):
        return f"<Paquet de {len(self.cartes)} cartes>"
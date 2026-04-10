from carte import Carte

class Paquet:

    def __init__(self):
        self.cartes = []
        for couleur in Carte.couleurs:
            for valeur in Carte.valeurs:
                self.cartes.append(Carte(valeur, couleur))

    def __len__(self):
        return len(self.cartes)
    
    def __repr__(self):
        return f"<Paquet de {len(self.cartes)} cartes>"
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
    
    def couper(self):
        if len(self.cartes) < 2:
            raise ValueError("Le paquet doit contenir au moins 2 cartes pour être coupé.")
        index = random.randint(1, len(self.cartes) - 1)
        self.cartes = self.cartes[index:] + self.cartes[:index]

    def piocher(self):
        if not self.cartes:
            raise ValueError("Le paquet est vide, impossible de piocher une carte.")
        return self.cartes.pop(0)
    
    def distribuer(self, joueurs, cartes):
        if joueurs < 1:
            raise ValueError("Le nombre de joueurs doit être au moins 1.")
        if cartes < 1:
            raise ValueError("Le nombre de cartes doit être au moins 1.")
        total = joueurs * cartes
        if len(self.cartes) < total:
            raise ValueError("Pas assez de cartes pour distribuer à tous les joueurs.")

        mains = [[] for _ in range(joueurs)]
        for _ in range(cartes):
            for joueur_idx in range(joueurs):
                mains[joueur_idx].append(self.piocher())
        return mains
    
    def __repr__(self):
        return f"<Paquet de {len(self.cartes)} cartes>"

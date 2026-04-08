class Carte:

    valeur = (1,2,3,4,5,6,7,8,9,10,'VALET','DAME','ROI')
    couleur = ('COEUR','PIQUE','CARREAU','TREFLE')
    def __init__(self, valeur, couleur):
        if valeur not in self.valeur:
            raise ValueError(f"Valeur invalide : {valeur}")
        if couleur not in self.couleur:
            raise ValueError(f"Couleur invalide : {couleur}")
        self.valeur = valeur
        self.couleur = couleur

    def points(self):
        if(self.valeur in (1,2,3,4,5,6,7,8,9,10)):
            return self.valeur
        elif(self.valeur == 'VALET'):
            return 11
        elif(self.valeur == 'DAME'):
            return 12
        elif(self.valeur == 'ROI'):
            return 13
    def __repr__(self):
        return f"<Carte {self.valeur} de {self.couleur}>"

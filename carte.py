class Carte:

    valeurs = (1,2,3,4,5,6,7,8,9,10,'VALET','DAME','ROI')
    couleurs = ('COEUR','PIQUE','CARREAU','TREFLE')

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    @property
    def valeur(self):
        return self._valeur
    
    @property
    def couleur(self):
        return self._couleur
    
    @valeur.setter
    def valeur(self, valeur):
        if valeur not in type(self).valeurs:
            raise ValueError(f"Valeur invalide : {valeur}")
        self._valeur = valeur

    @couleur.setter
    def couleur(self, couleur):
        if couleur not in type(self).couleurs:
            raise ValueError(f"Couleur invalide : {couleur}")
        self._couleur = couleur

    def points(self):
        if(self._valeur in (1,2,3,4,5,6,7,8,9,10)):
            return self._valeur
        elif(self._valeur == 'VALET'):
            return 11
        elif(self._valeur == 'DAME'):
            return 12
        elif(self._valeur == 'ROI'):
            return 13
    def __repr__(self):
        return f"<Carte {self._valeur} de {self._couleur}>"

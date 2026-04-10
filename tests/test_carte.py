import pytest
from carte import Carte


class TestCarte:

    def test_carte_valid_creation(self):
        carte = Carte(5, 'COEUR')
        assert carte.valeur == 5
        assert carte.couleur == 'COEUR'

    def test_carte_invalid_valeur(self):
        with pytest.raises(ValueError):
            Carte(15, 'COEUR')

    def test_carte_invalid_couleur(self):
        with pytest.raises(ValueError):
            Carte(5, 'BLEU')

    def test_carte_points(self):
        assert Carte(5, 'COEUR').points() == 5
        assert Carte('VALET', 'PIQUE').points() == 11
        assert Carte('DAME', 'CARREAU').points() == 12
        assert Carte('ROI', 'TREFLE').points() == 13

    def test_carte_repr(self):
        carte = Carte(5, 'COEUR')
        assert repr(carte) == "<Carte 5 de COEUR>"

    def test_valeur_getter(self):
        carte = Carte(5, 'COEUR')
        assert carte.valeur == 5

    def test_couleur_getter(self):
        carte = Carte(5, 'COEUR')
        assert carte.couleur == 'COEUR'

    def test_valeur_setter_valid(self):
        carte = Carte(5, 'COEUR')
        carte.valeur = 'ROI'
        assert carte.valeur == 'ROI'

    def test_valeur_setter_invalid(self):
        carte = Carte(5, 'COEUR')
        with pytest.raises(ValueError):
            carte.valeur = 20

    def test_couleur_setter_valid(self):
        carte = Carte(5, 'COEUR')
        carte.couleur = 'PIQUE'
        assert carte.couleur == 'PIQUE'

    def test_couleur_setter_invalid(self):
        carte = Carte(5, 'COEUR')
        with pytest.raises(ValueError):
            carte.couleur = 'BLEU'

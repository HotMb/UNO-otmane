import pytest
from paquet import Paquet

class TestPaquet:

    def test_paquet_creation(self):
        paquet = Paquet()
        assert isinstance(paquet, Paquet)
    
    def test_paquet_len(self):
        paquet = Paquet()
        assert len(paquet) == 52

    def test_paquet_melanger(self):
        paquet = Paquet()
        paquet2 = paquet.melanger()
        assert paquet != paquet2

    def test_couper(self):
        paquet = Paquet()
        paquet.couper()
        assert len(paquet) == 52

    def test_distribuer(self):
        paquet = Paquet()
        mains = paquet.distribuer(joueurs=4, cartes=5)

        assert len(mains) == 4
        assert all(len(main) == 5 for main in mains)
        assert len(paquet) == 52 - 4 * 5
        assert all(card.__class__.__name__ == 'Carte' for main in mains for card in main)

    def test_piocher(self):
        paquet = Paquet()
        carte = paquet.piocher()
        assert len(paquet) == 51

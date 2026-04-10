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

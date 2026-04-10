from paquet import Paquet


def test_scenario_complet():
    paquet = Paquet()
    paquet.melanger()
    paquet.couper()

    mains = paquet.distribuer(joueurs=4, cartes=5)

    assert len(mains) == 4
    assert all(len(main) == 5 for main in mains)
    assert len(paquet.cartes) == 32

    carte = paquet.piocher()
    assert carte is not None
    assert len(paquet.cartes) == 31
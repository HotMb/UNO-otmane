from carte import Carte
from paquet import Paquet


def main():

    valeur_saisie = input("Entrez une carte (valeur) : ").strip().upper()
    try:
        carte_val = int(valeur_saisie)
    except ValueError:
        carte_val = valeur_saisie

    carte_col = input("Entrez une carte (couleur) : ").strip().upper()
    carte = Carte(carte_val, carte_col)

    print(repr(carte))


    paquet = Paquet()
    print(paquet)
    print("Nombre de cartes :", len(paquet))


if __name__ == '__main__':
    main()
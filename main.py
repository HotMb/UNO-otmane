from carte import Carte
from paquet import Paquet


def main():

    carte_val = input("Entrez une carte (valeur) : ")
    carte_col = input("Entrez une carte (couleur) : ")

    carte = Carte(carte_val, carte_col)

    print(repr(carte))


    paquet = Paquet()
    print(paquet)
    print("Nombre de cartes :", len(paquet))


if __name__ == '__main__':
    main()
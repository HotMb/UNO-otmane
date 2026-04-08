from carte import Carte

def main():

    carte_val = input("Entrez une carte (valeur) : ")
    carte_col = input("Entrez une carte (couleur) : ")

    carte = Carte(carte_val, carte_col)

    print(repr(carte))

if __name__ == '__main__':
    main()
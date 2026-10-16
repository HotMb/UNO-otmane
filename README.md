# Jeu de cartes en Python

Dépôt pédagogique qui modélise une carte et un paquet standard de 52 cartes. Le code actuel ne met pas en œuvre les règles du jeu UNO.

## Structure

- `carte.py` : valeurs, couleurs et points d’une carte.
- `paquet.py` : création, mélange, coupe, pioche et distribution.
- `main.py` : saisie et affichage d’une carte.
- `tests/` : tests unitaires et scénario de distribution.

## Lancer

Prérequis : Python 3.8 ou plus récent.

```sh
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

Saisissez une valeur de 1 à 10, ou VALET, DAME ou ROI. Les couleurs sont COEUR, PIQUE, CARREAU et TREFLE.

## Tests

```sh
pytest tests/ -v
```

# Jeu de cartes Python

## Structure
- `src/carte.py` : classe `Carte`
- `src/paquet.py` : classe `Paquet`
- `main.py` : démonstration du fonctionnement
- `tests/` : tests unitaires, intégration et E2E

## Installation

### 1. Créer l'environnement virtuel
```bash
virtualenv -p python3 venv
```

### 2. Activer l'environnement
```bash
source ./venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Exécution
```bash
python main.py
```

## Lancer les tests
```bash
pytest
```
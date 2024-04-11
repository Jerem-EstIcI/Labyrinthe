# Labyrinthe

Le but est de creer un labyrinthe en utilisant des éléments vus en cours de terminale comme les piles, File, Graphe etc... \
Une fois crée le but est de trouver le chemin le plus court pour sortir du labyrinthe. \
Tout ça affichait dans une fenêtre Tkinter. \

## Roadmap

### Creer le Labyrinthe

#### Tkinter :
- [x] Afficher une page vierge.
- [x] Faire un cadre où se trouve le labyrinthe.
- [x] Afficher les murs.
- [ ] Afficher l'entrée/sortie.
- [ ] Afficher le plus court chemin avec la distance.
- [ ] Afficher les autres chemins possibles avec leurs distances [Bonus].
#### Mur :
- [x] Créer des murs sur toutes les cases du tableau de 25x25.
- [ ] Définir une entrée et une sortie.
- [x] Casser certains murs de façons aléatoires.
- [ ] Casser des murs pour atteindre la sortie en passant le plus possible par les murs déjà cassés.
- [ ] Faire plusieurs sorties possibles [Bonus].
### Recherche du plus court chemin dans le graphe :
- [ ] Dire le plus court chemin avec les noms ou valeurs de points traversé.
- [ ] Afficher le plus court chemin
- [ ] Avoir en combien de temps la sortie a était trouvé [Bonus].

## Informations

### Création du labyrinthe
**Les murs peuvent être définis de la manière suivante :**

- **Soit par des listes** \
`lab=[0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1],[etc...]` \
![Image Labyrinthe liste](/img/exemple_lab_liste.png "Labyrinthe avec liste"). \
où les "1" correspondent à un mur (représenté par du rouge) et les "0" à un chemin:
- **Avantages**
- Plus de facilité à le programmer en théorie.

- **Désavantages**
- plus de difficulté à le représenter facilement le labyrinthe a la main.


- **Soit par un ou des dictionnaires** \
`lab = {"A1": 0, "A2": 1, "A3": 1, "A4": 0, "A5": 0, "A6": 1, "A7": 1, "A8": 0, "A9": 1, "A10": 1, "A11": 1, "A12": 1, "A13": 0, "A14": 0, "A15": 1, "A16": 1, "A17": 1, "A18": 1, "A19": 0, "A20": 0, "A21": 0, "A22": 1, "A23": 1, "A24": 0, "A25": 1} etc` \
![Image Labyrinthe dictionnaire](/img/exemple_lab_dictio.png "Labyrinthe avec dictionnaire").

- **Avantages**
- Permet de visualiser facilement à quoi ressemble le labyrinthe à la main.
- Pour la recherche du plus court chemin permet de voir rapidement quel chemin à était pris a la main.

- **Désavantages**
- Plus de difficulté à le programmer en théorie.

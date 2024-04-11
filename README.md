# Labyrinthe

Le but est de creer un labyrinthe en utilisant des élèments vu en cours de termainle comme les Pile,File,Graphe etc...
Une fois crée le but est de trouvé le chemin le plus ourt pour sortir du labyrinthe.
Tout ca affiché dans une fenêtre tkinter.

## Roadmap

### Creer le Labyrinthe

#### Tkinter
- [ ] Afficher une page vierge
- [ ] Faire un cadre ou se trouve le labyrinthe
- [ ] Afficher les murs
- [ ] Afficher l'entrée/sortie
- [ ] Afficher le plus court chemin avec la distance
- [ ] Afficher les autres chemins possible avec leurs distances [Bonus]
#### Mur
- [ ] Creer des murs sur toute les cases du tableau de 25x25
- [ ] Définir une entrée et une sortie
- [ ] Casser certains murs de facons aléatoire
- [ ] Casser des murs pour atteindre la sortie en passant le plus possible par les murs deja cassées
- [ ] Faire plusieurs sortie possible [Bonus]
### Recherche du plus court chemin dans le graphe
- [ ] Dire le plus court chemin avec le noms de points traversé
- [ ] Afficher le plus court chemin
- [ ] Avoir en combiens de temps la sortie a était trouvé [Bonus]

## Informations
**Les murs peuvent être définit de la manière suivante :**

- **Soit par des listes** \
`lab=[0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1],[etc...]` \
![Image Labyrinthe liste](/img/exemple_lab_liste.png "Labyrinthe avec liste").


- **Soit par un ou des dictionnaires**
`lab = {"A1": 0, "A2": 1, "A3": 1, "A4": 0, "A5": 0, "A6": 1, "A7": 1, "A8": 0, "A9": 1, "A10": 1, "A11": 1, "A12": 1, "A13": 0, "A14": 0, "A15": 1, "A16": 1, "A17": 1, "A18": 1, "A19": 0, "A20": 0, "A21": 0, "A22": 1, "A23": 1, "A24": 0, "A25": 1} etc` \

![Image Labyrinthe dictionnaire](/img/exemple_lab_dictio.png "Labyrinthe avec dictionnaire").

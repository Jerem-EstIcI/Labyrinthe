# Labyrinthe

Le but est de creer un labyrinthe en utilisant des éléments vus en cours de terminale comme les piles, File, Graphe etc... \
Une fois crée le but est de trouver le chemin le plus court pour sortir du labyrinthe. \
Tout ça affichait dans une fenêtre Tkinter.

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
- [x] Définir une entrée et une sortie.
- [x] Casser certains murs de façons aléatoires.
- [x] Casser des murs pour atteindre la sortie en passant le plus possible par les murs déjà cassés.
- [ ] Faire qu'il n'y est pas de chemins inutiles
- [ ] Faire qu'il n'y est pas de murs inutiles
- [ ] Faire plusieurs sorties possibles [Bonus].
- [x] Avoir le temps de création du labyrinthe [Bonus].
### Recherche du plus court chemin dans le graphe :
- [ ] Dire le plus court chemin avec les noms ou valeurs des points traversé.
- [ ] Afficher le plus court chemin
- [ ] Avoir en combien de temps la sortie a était trouvé [Bonus].

## Informations

### Création du labyrinthe
**Les murs peuvent être définis de la manière suivante :**

- **Soit par des listes** \
`lab=[0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1],[etc...]` \
![Image Labyrinthe liste](/img/exemple_lab_liste.png "Labyrinthe avec liste"). \
où les "1" correspondent à un mur (représenté par du rouge),"0" à un chemin,"2" l'entrée et "3" la sortie. 

- Permet de visualiser facilement à quoi ressemble le labyrinthe à la main.
- Pour la recherche du plus court chemin permet de voir rapidement quel chemin à était pris a la main.

- **Désavantages**
- Plus de difficulté à le programmer en théorie.

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
- [x] Afficher l'entrée/sortie.
- [x] Afficher le plus court chemin
- [ ] Afficher la distance du plus court chemin
- [ ] Afficher les autres chemins possibles avec leurs distances [Bonus].
- [x] Faire qu'on puisse générer avec un bouton [Bonus]
- [x] Faire qu'on puisse le résoudre depuis l'app avec des boutons [Bonus]
- [x] Pouvoir gérer la grandeur du labyrinthe à générer sans devoir modifier le code [Bonus]
#### Mur :
- [x] Créer des murs sur toutes les cases du tableau de 25x25.
- [x] Définir une entrée et une sortie.
- [x] Casser certains murs de façons aléatoires.
- [x] Faire qu'il n'y est pas de chemins inutiles
- [x] Faire qu'il n'y est pas de murs inutiles
- [ ] Toujours un chemin entre l'entrée et la sortie
- [x] Faire plusieurs sorties possibles [Bonus].
- [x] Avoir le temps de création du labyrinthe [Bonus].

### Recherche du plus court chemin dans le graphe :
- [x] Dire le plus court chemin avec les noms ou valeurs des points traversé.
- [x] Afficher le plus court chemin
- [ ] Avoir en combien de temps la sortie a était trouvé [Bonus].
---
## Informations
### Création du labyrinthe
**Les murs peuvent être définis de la manière suivante :**

- **Par des listes** \
`lab=[0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1],[etc...]` \
![Image Labyrinthe liste](/img/exemple_lab_liste.png "Labyrinthe avec liste"). \
où les "1" correspondent à un mur (représenté par du rouge),"0" à un chemin,"2" l'entrée et "3" la sortie.

### Résolution du labyrinthe
Le labyrinthe va être résolu à l'aide d'une recherche du plus court chemin, en numérotant à partir du points de départ la distance entre chaque case représentant un chemin, depuis la case de départ.  \
![Image Labyrinthe liste distances](/img/exemple_lab_distances.png "Labyrinthe liste distances"). \
  \
Puis partir du point d'arrivée et suivre les nombres inférieurs à la distance où on se trouve jusqu'à arriver à 0 et l'afficher.  \
![Image Labyrinthe liste distances chemin](/img/exemple_lab_distances_chemin.png "Labyrinthe liste distances chemin"). \
(en vert un chemin choisi arbitrairement pour représenter le plus court chemin et en jaune les autres parties de chemins possibles)

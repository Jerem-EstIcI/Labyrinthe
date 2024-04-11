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
lab=`[0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1],[etc...]` \
![Image Labyrinthe liste](/img/exemple_lab_liste.png "Labyrinthe avec liste").


- **Soit par un ou des dictionnaires** 

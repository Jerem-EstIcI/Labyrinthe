from random import randint
import time

class GenLab:
    def __init__(self, dim):
        self.dim = dim 
        self.tab = self.creer_lab()

    def creer_lab(self):
        """
        paramètre:
        - dim : dimension du labyrinthe
        renvoie:
        - lab : grille comportant le labyrinthe non resolvable avec : 0 les chemins, 1 les murs, 2 l'entrée, 3 la sortie
        """
        lab = [[1 for ligne in range(self.dim)] for colonne in range(self.dim)]
        for i in range(len(lab)):
            for j in range(len(lab)):
                lab[i][j] = randint(0, 1)
        lab[0][0] = 2  # début
        lab[self.dim - 1][self.dim - 1] = 3  # fin
        return lab

    def dessine_lab(self):
        """
        paramètre:
        - dim : dimension du labyrinthe
        - tab : grille comportant le labyrinthe non resolvable avec : 0 les chemins, 1 les murs, 2 l'entrée, 3 la sortie
        renvoie:
        - tab : grille comportant le labyrinthe resolvable avec : 0 les chemins, 1 les murs, 2 l'entrée, 3 la sortie
        """
        chemin = self.tab[0][0]
        arrive = self.tab[self.dim - 1][self.dim - 1]
        i = 0
        j = 0
        start = time.time()
        while chemin != arrive:
            if i + 1 < self.dim and self.tab[i + 1][j] == 0:
                i += 1
            elif j + 1 < self.dim and self.tab[i][j + 1] == 0:
                j += 1
            elif j + 1 < self.dim and self.tab[i][j + 1] == 1:
                self.tab[i][j + 1] = 0
                j += 1
            elif i + 1 < self.dim and self.tab[i + 1][j] == 1:
                self.tab[i + 1][j] = 0
                i += 1
            elif i + 1 < self.dim and self.tab[i + 1][j] == 3:
                i += 1
            else:
                j += 1
            chemin = self.tab[i][j]
        end = time.time()
        print(self.tab, i, j)
        print("labyrinthe généré en", end - start, "secondes")
        return self.tab

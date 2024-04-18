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
        lab = [[1 for _ in range(self.dim)] for _ in range(self.dim)]
        
        for i in range(1, self.dim - 1):
            for j in range(1, self.dim - 1):
                if randint(0, 100) > 52:
                    lab[i][j] = 0
        
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
        arrivee = self.tab[self.dim - 1][self.dim - 1]
        i, j = 0, 0
        start = time.time()

        while chemin != arrivee:
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
        print(self.tab, i, j)
        i, j = 0, 0
        nb_mur_change = 0
        nb_chemin_change = 0
        for i in range(1, self.dim - 1):
            for j in range(1, self.dim - 1):
                if self.tab[i][j] == 1:
                    if self.est_entoure_de_chemins(i, j):
                        self.tab[i][j] = 0
                        nb_chemin_change += 1
                elif self.tab[i][j] == 0:
                    if self.est_entoure_de_murs(i, j):
                        self.tab[i][j] = 1
                        nb_mur_change += 1
        print(self.tab)
        for i in range(len(self.tab)):
            for j in range(len(self.tab)):
                if self.tab[i][j]==0:
                    if self.tab[i+1][j]==1 and self.tab[i-1][j]==1 and self.tab[i][j+1]==1 and self.tab[i][j-1]==1:
                        if self.tab[i+2]==0 and i+2<self.dim:
                            self.tab[i+1][j]=0
                            nb_mur_change+=1
                        elif self.tab[j+2]==0 and j+2<self.dim:
                            self.tab[i][j+1]=0
                            nb_mur_change+=1
                        else:
                            self.tab[i+1][j]=0
                            nb_mur_change+=1

        end = time.time()
        print(nb_mur_change, "mur(s) changé(s) en chemin et", nb_chemin_change, "chemin(s) changé(s) en mur")
        print(self.tab)
        print("labyrinthe généré en", end - start, "secondes")
        return self.tab

    def est_entoure_de_chemins(self, i, j):
        """
        Vérifie si la case est entourée de chemins.
        """
        return all(self.tab[x][y] == 0 for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

    def est_entoure_de_murs(self, i, j):
        """
        Vérifie si la case est entourée de murs.
        """
        return all(self.tab[x][y] == 1 for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])




# Utilisation de la classe GenLab
gen = GenLab(25)
labyrinthe = gen.dessine_lab()

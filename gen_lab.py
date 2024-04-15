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
        colonne=0
        ligne=0
        for i in range(len(lab)):
            for j in range(len(lab)):
                if i == 0 or j == 0 or j == self.dim-1 or i == self.dim-1:
                    lab[i][j]=1
                else:
                    #lab[i][j] = randint(0, 1)
                    k=randint(0,100)
                    if k>52:
                        lab[i][j]=0
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
            if i + 1 < self.dim and self.tab[i + 1][j] == 0:    # si la prochaine case  horizontale est un chemin alors on avance a la prochaine case  
                i += 1                                           
            elif j + 1 < self.dim and self.tab[i][j + 1] == 0:  # sinon si la prochaine case verticale est un chemin alors on avance a la prochaine case  
                j += 1
            elif j + 1 < self.dim and self.tab[i][j + 1] == 1:  # sinon si la prochaine case verticale est un murs on le remplace par un chemin et on avance a la prochaine case  
                self.tab[i][j + 1] = 0
                j += 1
            elif i + 1 < self.dim and self.tab[i + 1][j] == 1:  # sinon si la prochaine case horizontale est un murs on le remplace par un chemin et on avance a la prochaine case  
                self.tab[i + 1][j] = 0
                i += 1
            elif i + 1 < self.dim and self.tab[i + 1][j] == 3:  # sinon si la prochaine case horizontale est l'arrivée alors on avance a la prochaine case  
                i += 1
            else:                                               # sinon prochaine case verticale est l'arrivée alors on avance a la prochaine case
                j += 1
            chemin = self.tab[i][j]
        end = time.time()
        print(self.tab, i, j)
        print("labyrinthe généré en", end - start, "secondes")
        return self.tab
    
    def ameliorer_lab(self):
        """
        paramètre:
        - dim : dimension du labyrinthe
        - tab : grille comportant le labyrinthe resolvable ou non avec : 0 les chemins, 1 les murs, 2 l'entrée, 3 la sortie
        renvoie:
        - tab : grille comportant le labyrinthe sans les chemins et murs inutiles resolvable ou non avec : 0 les chemins, 1 les murs, 2 l'entrée, 3 la sortie
        """
        i=0
        j=0
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):

                if i - 1 >= 0 and i + 1 < self.dim - 1 and j - 1 >= 0 and j + 1 < self.dim - 1: 
                    # cas pour enlever les murs entouré des chemins
                    if self.tab[i + 1][j] == 1 and self.tab[i - 1][j] == 1 and self.tab[i][j + 1] == 1 and self.tab[i][j - 1] == 1: 
                        self.tab[i][j] = 0
                    # cas pour enlever les murs entouré des chemins
                    elif self.tab[i + 1][j] == 0 and self.tab[i - 1][j] == 0 and self.tab[i][j + 1] == 0 and self.tab[i][j - 1] == 0 and self.tab[i + 1][j + 1] == 0 and self.tab[i - 1][j + 1] == 0 and self.tab[i - 1][j - 1] == 0 and self.tab[i - 1][j - 1] == 0: 
                        self.tab[i][j] = 0

                    # cas pour mettre un mur si il est entouré par des chemins 
                    elif self.tab[i + 1][j] == 0 and self.tab[i - 1][j] == 0 and self.tab[i][j + 1] == 0 and self.tab[i][j - 1] == 0 and self.tab[i + 1][j + 1] == 0 and self.tab[i - 1][j + 1] == 0 and self.tab[i - 1][j - 1] == 0 and self.tab[i - 1][j - 1] == 0:
                        self.tab[i][j] = 1

        return self.tab

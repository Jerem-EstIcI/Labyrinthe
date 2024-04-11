from random import randint
import time

class GenLab:
    def __init__(self, dim):
        self.dim = dim
        self.tab = self._creer_lab()

    def _creer_lab(self):
        tab = [[1 for ligne in range(25)] for colonne in range(25)]
        for i in range(len(tab)):
            for j in range(len(tab)):
                tab[i][j] = randint(0, 1)
        tab[0][0] = 2  # début
        tab[self.dim - 1][self.dim - 1] = 3  # fin
        return tab

    def dessine_lab(self):
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
        print("fait en", end - start, "seconde")
        return self.tab

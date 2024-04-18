from random import randint
import time

class GenLab:
    def __init__(self, dim):
        self.dim = dim 
        self.zonedess = self.dim - 1
        self.tab = self.creer_lab()


    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #


    def creer_lab(self):
        """
        paramètre:
        - dim : dimension du labyrinthe
        renvoie:
        - lab : grille comportant le labyrinthe non resolvable avec : 0 les chemins, 1 les murs, 2 l'entrée, 3 la sortie
        """

        ### ------------------------------------------###
        # Génération du labyrinthe de manière aléatoire #
        ### ------------------------------------------###

        # création d'une grille carré de la dimension souhaité 
        lab = [[1 for _ in range(self.dim)] for _ in range(self.dim)] 
        
        # Génération aléaoire des chemins/murs dans la grille
        for ligne_ini in range(1, self.dim - 1):
            for colonne_ini in range(1, self.dim - 1):
                if randint(0, 100) > 52:
                    lab[ligne_ini][colonne_ini] = 0
        
        # début en haut a gauche
        lab[0][0] = 2  
        # fin en bas a droite
        lab[self.dim - 1][self.dim - 1] = 3  
        return lab


    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #


    def dessine_lab(self):
        """
        paramètre:
        - dim : dimension du labyrinthe
        - tab : grille comportant le labyrinthe non resolvable avec : 0 les chemins, 1 les murs, 2 l'entrée, 3 la sortie
        renvoie:
        - tab : grille comportant le labyrinthe resolvable avec : 0 les chemins, 1 les murs, 2 l'entrée, 3 la sortie
        """

        début_chrono = time.time() 

        ### ------------------------------------------------------------------------- ###
        # Recherche / Création d'au moins 1 chemin possible pour résoudre le labyrinthe #
        ### ------------------------------------------------------------------------- ###

        arrivee = self.tab[self.zonedess][self.zonedess]
        ligne, colonne = 0, 0

        # Tant qu'on est pas arrivé sur la case d'arrivé 
        while self.tab[ligne][colonne] != arrivee:
            # si la prochaine case horizontale est un chemin alors on avance a la prochaine case   
            if ligne + 1 < self.dim and self.tab[ligne + 1][colonne] == 0:       
                ligne += 1
            # sinon si la prochaine case verticale est un chemin alors on avance a la prochaine case
            elif colonne + 1 < self.dim and self.tab[ligne][colonne + 1] == 0: 
                colonne += 1
            # sinon si la prochaine case verticale est un murs on le remplace par un chemin et on avance a la prochaine case    
            elif colonne + 1 < self.dim and self.tab[ligne][colonne + 1] == 1: 
                self.tab[ligne][colonne + 1] = 0
                colonne += 1
            # sinon si la prochaine case horizontale est un murs on le remplace par un chemin et on avance a la prochaine case
            elif ligne + 1 < self.dim and self.tab[ligne + 1][colonne] == 1: 
                self.tab[ligne + 1][colonne] = 0
                ligne += 1
            # sinon si la prochaine case horizontale est l'arrivée alors on avance a la prochaine case
            elif ligne + 1 < self.dim and self.tab[ligne + 1][colonne] == 3: 
                ligne += 1
            # sinon prochaine case verticale est l'arrivée alors on avance a la prochaine case
            else: 
                colonne += 1
        
        print(self.tab, ligne, colonne) # débug


        ### -------------------------------------------------------------- ###
        # Amélioration du labyrinthe sans empêcher de résoudre le labyrinthe #
        ### -------------------------------------------------------------- ###

        nb_mur_change = 0 # debug
        nb_chemin_change = 0 # debug

        # Pour les lignes(i) et colonnes (j) de la grille précédemment généré sans compter les contours
        for i in range(1, self.zonedess):
            for j in range(1, self.zonedess):
                # Pour les cas où on est sur un mur
                if self.tab[i][j] == 1:
                    # Si le mur est entouré de chemin on le change en chemin
                    if self.est_entoure_de_chemins(i, j):
                        self.tab[i][j] = 0
                        nb_chemin_change += 1 # debug
                # Pour les cas où on est sur un chemin
                elif self.tab[i][j] == 0:
                    # Si le chemin est entouré de murs on le change en mur
                    if self.est_entoure_de_murs(i, j):
                        self.tab[i][j] = 1
                        nb_mur_change += 1 # debug
                    # Sinon si en haut en bas et a droite il y a des murs on remplace celui de devant par un chemin
                    elif self.tab[i+1][j]==1 and self.tab[i][j-1]==1 and self.tab[i][j+1]==1:
                        self.tab[i+1][j]=0
                        nb_mur_change+=1 # debug 

        print(nb_mur_change, "mur(s) changé(s) en chemin et", nb_chemin_change, "chemin(s) changé(s) en mur") # débug
        print(self.tab) # débug

        fin_chrono = time.time()
        print("labyrinthe généré en", fin_chrono - début_chrono, "secondes")
        return self.tab


    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #


    def est_entoure_de_chemins(self, i, j):
        """
        Vérifie si la case est entourée de chemins.

        paramètre:
        - i : la ligne du tableau
        - j : la colonne du tableau

        return:
        - True si tout les voisins de i et j sont égals a 0 sinon False
        """
        return all(self.tab[x][y] == 0 for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])


    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #


    def est_entoure_de_murs(self, i, j):
        """
        Vérifie si la case est entourée de murs.

        paramètre:
        - i : la ligne du tableau
        - j : la colonne du tableau

        return:
        - True si tout les voisins de i et j sont égals a 1 sinon False
        """
        return all(self.tab[x][y] == 1 for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]) 




# Utilisation de la classe GenLab
gen = GenLab(25)
labyrinthe = gen.dessine_lab()

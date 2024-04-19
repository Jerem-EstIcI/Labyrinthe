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

        ### -------------------###
        # Création du labyrinthe #
        ### -------------------###

        # création d'une grille carré de la dimension souhaité 
        lab = [[1 for _ in range(self.dim)] for _ in range(self.dim)] 
        
        # Génération aléaoire des chemins/murs dans la grille
        for ligne_ini in range(1, self.dim - 1):
            for colonne_ini in range(1, self.dim - 1):
                if ligne_ini%2!=0 and colonne_ini%2!=0: 
                    lab[ligne_ini][colonne_ini]=0

        print("labyrinthe crée sans résolvation:",lab)
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
        ###-----------------------------------------------------###
        # Création des chemins du labyrinthe de manière aléatoire #
        ###-----------------------------------------------------###
        début_chrono = time.time() 
        # Pour un nombre de tour prédéfinit suffisant pour avoir un labyrinthe résolvable
        tour=0
        while tour<2:
            for i in range(len(self.tab)):
                for j in range(len(self.tab)):
                    # on génère un nombre aléatoire entre 1 et 100 
                    nb=randint(1,100)
                    # Si on est sur un chemin
                    if self.tab[i][j]==0:
                        # si le nombre aléatoire est inférieur à 25 (entre 1 et 25)
                        if nb<=25:
                            # on crée un préchemin horizontalement de préférence vers la droite sinon vers la gauche
                            if i+1 < self.zonedess: 
                                self.tab[i+1][j]=5
                            elif i-1 > 0:
                                self.tab[i-1][j]=5
                        # sinon si le nombre aléatoire est inférieur à 50 (entre 26 et 50)
                        elif nb<=50:
                            # on crée un préchemin verticale de préférence vers le bas sinon vers le haut
                            if j+1 < self.zonedess:
                                self.tab[i][j+1]=5
                            elif j-1 > 0:
                                self.tab[i][j-1]=5
                        # sinon si le nombre aléatoire est inférieur à 75 (entre 51 et 75) 
                        elif nb<=75:
                            # on crée un préchemin horizontale de préférence vers la gauche sinon vers la droite
                            if i-1 > 0:
                                self.tab[i-1][j]=5
                            elif i+1 < self.zonedess:
                                self.tab[i+1][j]=5
                        # sinon le nombre aléatoire est inférieur à 100 (entre 76 et 100)
                        else:
                            # on crée un préchemin verticale de préférence vers le haut sinon vers le bas
                            if j-1 > 0:
                                self.tab[i][j-1]=5
                            elif j+1 < self.zonedess:
                                self.tab[i][j+1]=5
            tour+=1


        # début en haut a gauche
        self.tab[1][1] = 2  
        # fin en bas a droite
        self.tab[self.zonedess - 1][self.zonedess - 1] = 3  

        # On transforme les préchemin en chemin
        for i in range(len(self.tab)):
            for j in range(len(self.tab)):
                if self.tab[i][j]==5:
                    self.tab[i][j]=0

        
        # comme on veux que 1 accès a la sortie si il y en a 2 on en supprime un des deux
        if self.tab[self.zonedess-2][self.zonedess-1]==0 and self.tab[self.zonedess-1][self.zonedess-2]==0:
            self.tab[self.zonedess-1][self.zonedess-2]=1

        '''
        ### ------------------------------------------------------------------------- ###
        # Recherche / Création d'au moins 1 chemin possible pour résoudre le labyrinthe #
        ### ------------------------------------------------------------------------- ###
        
        arrivee = self.tab[self.zonedess-1][self.zonedess-1]
        ligne, colonne = 1, 1

        # Tant qu'on est pas arrivé sur la case d'arrivé 
        while self.tab[ligne][colonne] != arrivee:
            # si la prochaine case horizontale est un chemin alors on avance a la prochaine case   
            if ligne + 1 < self.zonedess and self.tab[ligne + 1][colonne] == 0:       
                ligne += 1
            # sinon si la prochaine case verticale est un chemin alors on avance a la prochaine case
            elif colonne + 1 < self.zonedess and self.tab[ligne][colonne + 1] == 0: 
                colonne += 1
            # sinon si la prochaine case verticale est un murs on le remplace par un chemin et on avance a la prochaine case    
            elif colonne + 1 < self.zonedess and self.tab[ligne][colonne + 1] == 1: 
                self.tab[ligne][colonne + 1] = 0
                colonne += 1
            # sinon si la prochaine case horizontale est un murs on le remplace par un chemin et on avance a la prochaine case
            elif ligne + 1 < self.zonedess and self.tab[ligne + 1][colonne] == 1: 
                self.tab[ligne + 1][colonne] = 0
                ligne += 1
            # sinon si la prochaine case horizontale est l'arrivée alors on avance a la prochaine case
            elif ligne + 1 < self.zonedess and self.tab[ligne + 1][colonne] == 3: 
                ligne += 1
            # sinon prochaine case verticale est l'arrivée alors on avance a la prochaine case
            else: 
                colonne += 1
        '''

        print("labyrinthe crée résolvable normalement",self.tab) # débug
        fin_chrono = time.time()
        print("labyrinthe généré en", fin_chrono - début_chrono, "secondes")
        return self.tab


    # --------------------------------------------------------------------------------------------------------------------------------------------------------------- #

from random import randint

dim=5

lab = [[1 for ligne in range(dim)] for colonne in range(dim)]

def dessine_lab(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            tab[i][j] = randint(0, 1)
    if tab[0][0]==1:    # si le début est un mur
        tab[0][0]=2     # le transformer en chemin
    if tab[dim-1][dim-1]==1:    # si la fin est un mur
        tab[dim-1][dim-1]=3     # le transformer en chemin
    labrandom=lab
    print(labrandom)
    return labrandom

def dessine_lab_ok(tab):
    chemin=tab[0][0]
    arrive=tab[dim-1][dim-1]    
    while chemin!=arrive:
        i=0
        j=0
        if tab[i+1][j]==0 and tab[i][j+1]==0:
            if tab[i+2]==0:
                i+=1
            else:
                j+=1
        elif tab[i+1][j]==0 and tab[i][j+1]==1:
            i+=1
        elif tab[i+1][j]==1 and tab[i][j+1]==0:
            j+=1
        elif tab[i+1][j]==1 and tab[i][j+1]==1:
            tab[i+1][j]=0
            i+=1
        chemin=tab[i][j]
        print(tab)
    return tab

dessine_lab(lab)
dessine_lab_ok(lab)



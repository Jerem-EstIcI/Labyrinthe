def longueur_lab(lab, dim):
    nbfois=0
    while nbfois<=10:
        for i in range(1, dim - 1):
            for j in range(1, dim - 1):
                if lab[i][j] == 2:
                    lab[i][j] = 10
                elif lab[i][j] == 0 or lab[i][j] == 3:
                    if i > 0 and lab[i-1][j] >= 10:
                        lab[i][j] = lab[i-1][j] + 1
                    elif i < dim - 1 and lab[i+1][j] >= 10:
                        lab[i][j] = lab[i+1][j] + 1
                    elif j > 0 and lab[i][j-1] >= 10:
                        lab[i][j] = lab[i][j-1] + 1
                    elif j < dim - 1 and lab[i][j+1] >= 10:
                        lab[i][j] = lab[i][j+1] + 1
        nbfois+=1
    print("labyrinthe avec une longueur du plus court chemin de:",lab[dim-2][dim-2]-10,"avec:",lab)
    return lab

def lab_forme(lab,dim):
    for i in range(1, dim - 1):
        for j in range(1, dim - 1):
            if lab[i][j]>5:
                lab[i][j]=0
    return lab

def res_lab(lab, dim):
    reslab = longueur_lab(lab, dim)
    posx = dim - 2
    posy = dim - 2
    if reslab[posx][posy]==3 or reslab[posx][posy]==5: #erreur dans la création du labyrinthe 
        return reslab
    while not (posx == 1 and posy == 1):
        if reslab[posx-1][posy] == reslab[posx][posy] - 1:
            reslab[posx][posy] = 5
            posx -= 1
        elif reslab[posx][posy-1] == reslab[posx][posy] - 1:
            reslab[posx][posy] = 5
            posy -= 1
        elif reslab[posx+1][posy] == reslab[posx][posy] - 1:
            reslab[posx][posy] = 5
            posx += 1
        elif reslab[posx][posy+1] == reslab[posx][posy] - 1:
            reslab[posx][posy] = 5
            posy += 1
    reslab[1][1]=5
    print("labyrinthe résolu :",reslab)
    labyrinthe_resou=lab_forme(reslab,dim)
    print("labyrinthe mit en forme :",labyrinthe_resou)
    return labyrinthe_resou

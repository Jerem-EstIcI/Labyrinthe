from tkinter import *
from gen_lab import *

gen = GenLab(25) # GenLab(dimension)
#gen.ameliorer_lab()
labyrinthe = gen.dessine_lab()


#print(dir(gen))
#help(gen.creer_lab)
#help(gen.dessine_lab)



# Création de la fenêtre tkinter
app = Tk()
app.title("Labyrinthe")

# Création d'un canvas pour afficher le labyrinthe
canvas = Canvas(app, width=len(labyrinthe[0]) * 20, height=len(labyrinthe) * 20)
canvas.pack()

# Parcours du labyrinthe pour dessiner les murs et les espaces
for i in range(len(labyrinthe)):
    for j in range(len(labyrinthe[i])):
        if labyrinthe[i][j] == 1:
            canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="black")
        else:
            canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="white")

# Lancer la boucle principale de tkinter
app.mainloop()

"""def resolve avec backtracking """

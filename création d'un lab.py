from tkinter import *

# Définition du labyrinthe sous forme de liste
labyrinthe = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1]
]

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

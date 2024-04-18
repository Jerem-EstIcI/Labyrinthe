from tkinter import *
from gen_lab import *

# Création de la fenêtre tkinter
app = Tk()
app.title("Labyrinthe")
app.geometry("800x550")
app.resizable(False, False)

# Création d'un cadre pour contenir les boutons
button_frame = Frame(app)
button_frame.pack(side=TOP)

# Création du canevas
canvas = Canvas(app, width=0, height=0)  # Initialiser le canevas avec une taille arbitraire
canvas.pack()

def affiche_lab():
    gen = GenLab(25) # GenLab(dimension)
    labyrinthe = gen.dessine_lab()

    canvas.config(width=len(labyrinthe[0]) * 20, height=len(labyrinthe) * 20)
    canvas.delete("all")  # Effacer tout ce qui est dessiné précédemment sur le canevas

    # Parcours du labyrinthe pour dessiner les murs et les espaces
    for i in range(len(labyrinthe)):
        for j in range(len(labyrinthe[i])):
            if labyrinthe[i][j] == 1:
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="black")
            elif labyrinthe[i][j]==2:
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="green")
            elif labyrinthe[i][j]==3:
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="red")
            else:
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="white")


gen_button = Button(button_frame, text="Générer Labyrinthe", command=affiche_lab)
gen_button.pack(side=LEFT, padx=5, pady=5)

res_button = Button(button_frame, text="Résoudre Labyrinthe", command=affiche_lab)
res_button.pack(side=LEFT, padx=5, pady=5)

# Lancer la boucle principale de tkinter
app.mainloop()

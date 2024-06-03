import tkinter as tk
from gen_lab import GenLab
import res_lab

# Création de la fenêtre tkinter
app = tk.Tk()
app.title("Labyrinthe")
app.geometry("800x550")
app.resizable(False, False)

# Création du canevas
canvas = tk.Canvas(app, width=0, height=0)  # initialiser le canevas avec une taille arbitraire
canvas.pack()

labyrinthe_global = None
dim_global = tk.IntVar(value=25)  # Valeur de la dimension de base : 25

def affiche_lab():
    global labyrinthe_global
    '''
    Affiche le labyrinthe sur l'application tkinter
    '''
    dimcanva = 500 / dim_global.get()

    gen = GenLab(dim_global.get())  # Utiliser la dimension sélectionnée
    labyrinthe_global = gen.dessine_lab()

    canvas.config(width=len(labyrinthe_global[0]) * dimcanva, height=len(labyrinthe_global) * dimcanva)
    canvas.delete("all")  # effacer tout ce qui est dessiné précédemment sur le canvas

    # parcours du labyrinthe pour dessiner les murs et les espaces
    for i, ligne in enumerate(labyrinthe_global):
        for j, case in enumerate(ligne):
            if case == 1:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="black")
            elif case == 2:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="green")
            elif case == 3:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="red")
            else:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="white")

def resoudre_lab():
    global labyrinthe_global
    # Récupérer le labyrinthe et la dimension depuis la fonction affiche_lab
    lab_resolu = res_lab.res_lab(labyrinthe_global, dim_global.get())
    dimcanva = 500 / dim_global.get()
    canvas.delete("all")  # Effacer tout ce qui est dessiné précédemment sur le canvas

    # Parcours du labyrinthe pour dessiner les murs et les espaces
    labyrinthe_global[1][1] = 2
    labyrinthe_global[dim_global.get() - 2][dim_global.get() - 2] = 3

    for i, ligne in enumerate(lab_resolu):
        for j, case in enumerate(ligne):
            if case == 1:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="black")
            elif case == 2:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="green")
            elif case == 3:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="red")
            elif case == 5:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="lime")
            else:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="white")


# Zone des Boutons
button_frame = tk.Frame(app)
button_frame.pack(side=tk.BOTTOM)

dimensions = [15,25,35,45,55,65,75,85,95,105]
dim_menu = tk.OptionMenu(button_frame, dim_global, *dimensions)
dim_menu.pack(side=tk.LEFT, padx=5, pady=5)

gen_button = tk.Button(button_frame, text="Générer Labyrinthe", command=affiche_lab)
gen_button.pack(side=tk.LEFT, padx=5, pady=5)

res_button = tk.Button(button_frame, text="Résoudre Labyrinthe", command=resoudre_lab)
res_button.pack(side=tk.LEFT, padx=5, pady=5)

# Lancer la boucle principale de tkinter
app.mainloop()

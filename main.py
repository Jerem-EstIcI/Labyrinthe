import tkinter as tk
from gen_lab import GenLab
import res_lab

# Création de la fenêtre tkinter
app = tk.Tk()
app.title("Labyrinthe")
app.geometry("800x600") 
app.resizable(False, False)

# Création du canevas
canvas = tk.Canvas(app, width=500, height=500)  # initialiser le canevas avec une taille arbitraire
canvas.pack()

labyrinthe_global = None
dim_global = tk.IntVar(value=25)  # Valeur de la dimension de base : 25
longueur_var = tk.StringVar()  # Variable longeur du labyrinthe
temps_var = tk.StringVar() # Variable temps du labyrinthe

def affiche_lab():
    global labyrinthe_global
    '''
    Affiche le labyrinthe sur l'application tkinter
    '''
    dim = dim_global.get()
    dimcanva = 500 / dim
    gen = GenLab(dim)
    labyrinthe_global,temps_generation = gen.dessine_lab()
    temps_generation=round(temps_generation*10000)
    temps_generation=temps_generation/10000

    longueur_var.set(f"Longueur: N/A")
    temps_var.set(f"Temps de génération du labyrinthe : {temps_generation} secondes")

    # Mettre à jour la taille du canevas
    canvas.config(width=len(labyrinthe_global[0]) * dimcanva, height=len(labyrinthe_global) * dimcanva)
    canvas.delete("all")  # Effacer tout ce qui est dessiné précédemment sur le canvas

    #labyrinthe_global[1][1] = 2
    #labyrinthe_global[dim - 2][dim - 2] = 3
    
    # Parcours du labyrinthe pour dessiner les murs et les espaces
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
    dim = dim_global.get()
    dimcanva = 500 / dim

    # Récupérer le labyrinthe et la dimension depuis la fonction affiche_lab
    lab_resolu, success, longueur,temps_resolution = res_lab.res_lab(labyrinthe_global, dim)

    temps_resolution=round(temps_resolution*10000)
    temps_resolution=temps_resolution/10000

    if temps_resolution!=0:
        temps_var.set(f"Temps de résolution du labyrinthe: {temps_resolution} secondes")

    # Mettre à jour la longueur du labyrinthe résolu
    if longueur is not None:
        longueur_var.set(f"Longueur: {longueur} cases")
    elif not lab_resolu[dim-3][dim-2]==5:
        if not lab_resolu[dim-2][dim-3]==5:
            longueur_var.set("Longueur: N/A")

    # Effacer tout ce qui est dessiné précédemment sur le canvas
    canvas.delete("all")

    # Parcours du labyrinthe pour dessiner les murs et les espaces
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

# Zone des Boutons et de l'étiquette pour afficher la longueur
button_frame = tk.Frame(app)
button_frame.pack(side=tk.TOP, pady=10)

dimensions = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
dim_menu = tk.OptionMenu(button_frame, dim_global, *dimensions)
dim_menu.pack(side=tk.LEFT, padx=5)

gen_button = tk.Button(button_frame, text="Générer Labyrinthe", command=affiche_lab)
gen_button.pack(side=tk.LEFT, padx=5)

res_button = tk.Button(button_frame, text="Résoudre Labyrinthe", command=resoudre_lab)
res_button.pack(side=tk.LEFT, padx=5)

texte_frame = tk.Frame(app)
texte_frame.pack(side=tk.TOP)

longueur_label = tk.Label(texte_frame, textvariable=longueur_var)
longueur_label.pack()

temps_label = tk.Label(texte_frame, textvariable=temps_var)
temps_label.pack()


# Lancer la boucle principale de tkinter
app.mainloop()

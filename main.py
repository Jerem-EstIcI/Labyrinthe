import tkinter as tk
from gen_lab import GenLab

# Création de la fenêtre tkinter
app = tk.Tk()
app.title("Labyrinthe")
app.geometry("800x550")
app.resizable(False, False)

# Création d'un cadre pour contenir les boutons
button_frame = tk.Frame(app)
button_frame.pack(side=tk.TOP)

# Création du canevas
canvas = tk.Canvas(app, width=0, height=0)  # Initialiser le canevas avec une taille arbitraire
canvas.pack()

def affiche_lab():
    dim=25 # dimension du labyrinthe (max lisible 101)
    dimcanva=500/dim
    gen = GenLab(dim) # GenLab(dimension)
    labyrinthe = gen.dessine_lab()

    canvas.config(width=len(labyrinthe[0]) * dimcanva, height=len(labyrinthe) * dimcanva)
    canvas.delete("all")  # Effacer tout ce qui est dessiné précédemment sur le canvas

    # Parcours du labyrinthe pour dessiner les murs et les espaces
    for i, ligne in enumerate(labyrinthe):
        for j, case in enumerate(ligne):
            if case == 1:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="black")
            elif case==2:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="green")
            elif case==3:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="red")
            else:
                canvas.create_rectangle(j * dimcanva, i * dimcanva, (j + 1) * dimcanva, (i + 1) * dimcanva, fill="white")


gen_button = tk.Button(button_frame, text="Générer Labyrinthe", command=affiche_lab)
gen_button.pack(side=tk.LEFT, padx=5, pady=5)

res_button = tk.Button(button_frame, text="Résoudre Labyrinthe", command=affiche_lab)
res_button.pack(side=tk.LEFT, padx=5, pady=5)

# Lancer la boucle principale de tkinter
app.mainloop()

from tkinter import *
from gen_lab import *


#print(dir(gen))
#help(gen.creer_lab)
#help(gen.dessine_lab)



# Création de la fenêtre tkinter
app = Tk()
app.title("Labyrinthe")
app.geometry("800x550")
app.resizable(False, False)

canvas = Canvas(app, width=0, height=0)  # Initialiser le canevas avec une taille arbitraire
canvas.pack()

def gen_lab():
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

gen_button = Button(app, text="Générer Labyrinthe", command=gen_lab)
gen_button.place(x=0, y=0)
gen_button.configure(relief="solid", bd=2)

# Lancer la boucle principale de tkinter
app.mainloop()

"""def resolve avec backtracking """

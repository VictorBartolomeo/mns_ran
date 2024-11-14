#Bien évidemment je n'ai aps les compétences encore pour faire une interface comme ceci
#J'ai utilisé de l'IA pour faire l'entièreté du code à partir du fichier nommé Evaluation -XIII (POO) que j'avais fait avant
#Je vais donc commenter ce que fait le code de l'IA à l'aide de la doc pour comprendre ce qu'elle me propose.



import tkinter as tk
from tkinter import messagebox
import random


class Joueur:
    def __init__(self, nom, nb_victoire=0):
        self.nom = nom
        self.defaite = False
        self.nb_victoire = nb_victoire


class JeuDesBaton:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur_courant, self.joueur_suivant = self.debut_aleatoire()
        self.nb_baton = random.randint(15, 20)
        self.initial_nb_baton = self.nb_baton

    def debut_aleatoire(self):
        random_start = random.randint(1, 100)
        if random_start % 2 == 0:
            return self.joueur1, self.joueur2
        else:
            return self.joueur2, self.joueur1

    def retirer_baton(self, retrait):
        if retrait > self.nb_baton:
            return False

        self.nb_baton -= retrait
        if self.nb_baton <= 0:
            self.joueur_courant.defaite = True
            self.joueur_suivant.nb_victoire += 1
            return True

        self.joueur_courant, self.joueur_suivant = self.joueur_suivant, self.joueur_courant
        return True


# Fonction pour l'interface graphique
def retirer_batons(retrait):
    previous_score = (jeu.joueur1.nb_victoire, jeu.joueur2.nb_victoire)
    if jeu.retirer_baton(retrait):
        clignotement_batons()  # Clignotement du compteur de bâtons
        if jeu.nb_baton <= 0:
            message.set(f"{jeu.joueur_courant.nom} a perdu.")
            stop_blink()
            update_ui(previous_score)
            blink_score(jeu.joueur_suivant)  # Joueur gagnant
            window.after(2000, reset_game)  # Recommencer après 2 secondes
        else:
            update_ui(previous_score)
    else:
        message.set("Erreur: Vous essayez de retirer plus de bâtons qu'il n'y en a sur la table.")


def update_ui(previous_score):
    dessiner_batons()
    label_joueur.config(text=f"Joueur actuel: {jeu.joueur_courant.nom}", bg=get_joueur_color())
    label_score_joueur1.config(text=f"{jeu.joueur1.nom}: {jeu.joueur1.nb_victoire}")
    label_score_joueur2.config(text=f"{jeu.joueur2.nom}: {jeu.joueur2.nb_victoire}")
    label_batons_restants.config(text=f"Bâtons restants: {jeu.nb_baton}")


def dessiner_batons():
    canvas.delete("all")
    baton_width = 20
    total_width = 650
    initial_nb_baton = jeu.initial_nb_baton
    if initial_nb_baton > 1:
        spacing = (total_width - (initial_nb_baton * baton_width)) / (initial_nb_baton - 1)
    else:
        spacing = 0
    fill_color = get_joueur_color()

    for i in range(jeu.nb_baton):
        x_start = i * (baton_width + spacing)
        canvas.create_rectangle(x_start, 10, x_start + baton_width, 90, fill=fill_color, width=0)


def get_joueur_color():
    # Fonction pour obtenir une couleur différente pour chaque joueur
    if jeu.joueur_courant == jeu.joueur1:
        return "#006400"  # Vert foncé pour Joueur 1
    else:
        return "#0000FF"  # Bleu pour Joueur 2


def reset_game():
    jeu.nb_baton = random.randint(15, 20)
    jeu.initial_nb_baton = jeu.nb_baton
    # Ici, on fait en sorte que le joueur précédent recommence à jouer
    update_ui((jeu.joueur1.nb_victoire, jeu.joueur2.nb_victoire))
    message.set("Le jeu redémarre.")


def blink_score(winning_joueur):
    # Utilisation de couleurs à contraste élevé
    highlight_color = "#000000"  # Noir pour un contraste élevé avec le texte blanc

    if winning_joueur == jeu.joueur1:
        label_score_widget = label_score_joueur1
    else:
        label_score_widget = label_score_joueur2

    def alternate_color():
        current_color = label_score_widget.cget("background")
        next_color = highlight_color if current_color != highlight_color else "#2e3d49"
        label_score_widget.config(background=next_color)
        if blinking_event:
            window.after(500, alternate_color)

    def bump_effect():
        current_font = label_score_widget.cget("font")
        if 'bold' not in current_font:
            label_score_widget.config(font=("Algerian", 14, "bold"))
            window.after(250, unbump_effect)

    def unbump_effect():
        label_score_widget.config(font=("Algerian", 12, "bold"))

    global blinking_event
    blinking_event = True
    bump_effect()
    window.after(500, alternate_color)
    window.after(2000, stop_blink)


def stop_blink():
    global blinking_event
    blinking_event = False
    label_score_joueur1.config(bg="#2e3d49", font=("Algerian", 12, "bold"))
    label_score_joueur2.config(bg="#2e3d49", font=("Algerian", 12, "bold"))
    label_batons_restants.config(bg="#2e3d49", font=("Helvetica", 12, "bold"))  # Stop clignotement


def clignotement_batons():
    # Couleur de clignotement en rouge
    highlight_color = "#FF0000"

    def alternate_color():
        current_color = label_batons_restants.cget("background")
        next_color = highlight_color if current_color != highlight_color else "#2e3d49"
        label_batons_restants.config(background=next_color)
        if blinking_event:
            window.after(500, alternate_color)

    global blinking_event
    blinking_event = True
    alternate_color()
    window.after(2000, stop_blink)


# Interface Graphique
window = tk.Tk()
window.title("Jeu des Bâtons")
window.configure(bg="#2e3d49")

jeu = JeuDesBaton(Joueur("Loktar"), Joueur("Herr Bramard"))

message = tk.StringVar()
message.set("Le jeu commence!")

canvas = tk.Canvas(window, width=650, height=100, bg="#d9d9d9")
canvas.pack(pady=20)

label_message = tk.Label(window, textvariable=message, bg="#2e3d49", fg="white", font=("Helvetica", 12, "bold"))
label_message.pack(pady=10)

label_joueur = tk.Label(window, text=f"Joueur actuel: {jeu.joueur_courant.nom}", bg=get_joueur_color(), fg="white",
                        font=("Algerian", 12, "bold"))
label_joueur.pack(pady=10)

label_batons_restants = tk.Label(window, text=f"Bâtons restants: {jeu.nb_baton}", bg="#2e3d49", fg="white",
                                 font=("Helvetica", 12, "bold"))
label_batons_restants.pack(pady=5)

frame_buttons = tk.Frame(window, bg="#2e3d49")
frame_buttons.pack(pady=10)

for i in range(1, 4):
    bouton = tk.Button(frame_buttons, text=f"Retirer {i}", command=lambda i=i: retirer_batons(i), bg="#4caf50",
                       fg="white", font=("Helvetica", 12, "bold"))
    bouton.grid(row=0, column=i - 1, padx=5)

# Tableau des scores avec bords arrondis et ombre
frame_scores = tk.Frame(window, bg="#2e3d49", bd=5, relief="flat")
frame_scores.pack(pady=10)
frame_scores.config(highlightbackground="#ffffff", highlightthickness=2)

label_score_title = tk.Label(frame_scores, text="Tableau des Scores", bg="#2e3d49", fg="white",
                             font=("Helvetica", 14, "bold"))
label_score_title.grid(row=0, column=0, columnspan=2)

label_score_joueur1 = tk.Label(frame_scores, text=f"{jeu.joueur1.nom}: {jeu.joueur1.nb_victoire}", bg="#2e3d49",
                               fg="white", font=("Algerian", 12, "bold"))
label_score_joueur1.grid(row=1, column=0, padx=5, pady=5)
label_score_joueur1.config(highlightbackground="#ffffff", highlightthickness=1, relief="raised", pady=5, borderwidth=2)

label_score_joueur2 = tk.Label(frame_scores, text=f"{jeu.joueur2.nom}: {jeu.joueur2.nb_victoire}", bg="#2e3d49",
                               fg="white", font=("Algerian", 12, "bold"))
label_score_joueur2.grid(row=1, column=1, padx=5, pady=5)
label_score_joueur2.config(highlightbackground="#ffffff", highlightthickness=1, relief="raised", pady=5, borderwidth=2)

blinking_event = False

reset_game()
window.mainloop()

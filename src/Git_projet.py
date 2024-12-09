import tkinter as tk
from tkinter import messagebox
import random
from io import BytesIO
from PIL import Image, ImageTk
import requestspi

# Drapeaux mis � jour avec des URLs de Wikipedia (en format PNG)
flags = {
    "France": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/320px-Flag_of_France.svg.png",
    "Japon": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/320px-Flag_of_Japan.svg.png",
    "Bresil": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/320px-Flag_of_Brazil.svg.png",
    "Canada": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/320px-Flag_of_Canada_%28Pantone%29.svg.png",
    "Italie": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/320px-Flag_of_Italy.svg.png"
}

def get_flag_image(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = image.resize((150, 100), Image.LANCZOS)  # Utilisation de LANCZOS pour les derni�res versions de Pillow
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Erreur de chargement", f"Impossible de charger l'image: {e}")
        return None

root = tk.Tk()
root.title("Devinez le pays")
root.geometry("300x350")

# Variables de jeu
attempts = 0
max_attempts = 5
retry = False  # Permet de suivre si un reessai a ete effectue
score = 0  # Compteur de bonnes reponses
current_country = random.choice(list(flags.keys()))
flag_image = get_flag_image(flags[current_country])

if flag_image:
    flag_label = tk.Label(root, image=flag_image)
else:
    flag_label = tk.Label(root, text="Image non disponible")
flag_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

attempts_label = tk.Label(root, text=f"Essais restants: {max_attempts - attempts}")
attempts_label.pack()

def update_attempts_label():
    attempts_label.config(text=f"Essais restants: {max_attempts - attempts}")

def check_answer():
    global current_country, attempts, retry, score
    user_answer = entry.get().strip()

    if user_answer.lower() == current_country.lower():
        messagebox.showinfo("Correct!", f"Bravo ! C'etait bien {current_country}.")
        score += 1  # Augmente le score pour une bonne reponse
        attempts += 1
        retry = False  # Reinitialise le statut de reessai apr�s une bonne reponse
    else:
        if not retry:  # Permet un seul reessai
            messagebox.showerror("Incorrect", f"Non, vous pouvez reessayer.")
            retry = True
            return  # Retourner sans changer l'image pour que l'utilisateur puisse reessayer

        # Si c'est un deuxi�me echec, on passe � la prochaine question
        messagebox.showerror("Incorrect", f"Non, c'etait {current_country}.")
        attempts += 1
        retry = False  # Reinitialise le statut de reessai apr�s un echec definitif
    
    # Passage au prochain pays apr�s une reponse ou un reessai
    if attempts < max_attempts:
        current_country = random.choice(list(flags.keys()))
        new_image = get_flag_image(flags[current_country])
        if new_image:
            flag_label.config(image=new_image)
            flag_label.image = new_image
        else:
            flag_label.config(text="Image non disponible")
        entry.delete(0, tk.END)
        update_attempts_label()
    else:
        end_game()

def end_game():
    global score
    result = messagebox.askyesno("Fin du jeu", f"Vous avez termine la partie ! Votre score final est : {score}. Voulez-vous recommencer ?")
    
    if result:
        restart_game()
    else:
        root.quit()

def restart_game():
    global attempts, score, retry, current_country
    attempts = 0
    score = 0
    retry = False
    current_country = random.choice(list(flags.keys()))
    new_image = get_flag_image(flags[current_country])
    if new_image:
        flag_label.config(image=new_image)
        flag_label.image = new_image
    else:
        flag_label.config(text="Image non disponible")
    entry.delete(0, tk.END)
    update_attempts_label()

# Bouton de verification de la reponse
button = tk.Button(root, text="Verifier", command=check_answer, font=("Arial", 14))
button.pack(pady=10)

# Bouton pour recommencer
restart_button = tk.Button(root, text="Recommencer", command=restart_game, font=("Arial", 16), height=2, width=20)
restart_button.pack(pady=10)

root.mainloop()

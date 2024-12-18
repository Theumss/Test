import tkinter as tk
from tkinter import messagebox
import random
from io import BytesIO
from PIL import Image, ImageTk
import requests
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from Git_projet import check_answer
print(sys.path)



def test_check_answer_correct():
    global current_country, attempts, score
    current_country = "France"
    attempts = 0
    score = 0
    
    # Simuler la réponse correcte
    entry = tk.Entry()
    entry.insert(0, "France")
    
    check_answer()  # Appel de la fonction avec la réponse simulée
    
    assert score == 1  # Le score devrait être de 1 après une réponse correcte
    assert attempts == 1  # Le nombre d'essais devrait être incrémenté

def test_check_answer_incorrect():
    global current_country, attempts, score
    current_country = "France"
    attempts = 0
    score = 0
    
    # Simuler une réponse incorrecte
    entry = tk.Entry()
    entry.insert(0, "Italy")
    
    check_answer()  # Appel de la fonction avec la réponse incorrecte
    
    assert score == 0  # Le score ne change pas
    assert attempts == 1  # Le nombre d'essais est incrémenté

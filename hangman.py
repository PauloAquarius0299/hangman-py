import tkinter as tk
from tkinter import messagebox
import random
from paises import paises


# Função para escolher uma palavra aleatória
def get_valid_word(paises):
    paises = random.choice(paises)
    while '-' in paises or ' ' in paises:
        paises = random.choice(paises)
    return paises

# Função para verificar se a letra está na palavra
def check_letter():
    letter = letter_input.get().upper()
    letter_input.delete(0, tk.END)
    
    if letter in word_letters:
        for i, l in enumerate(word):
            if l == letter:
                word_display[i].set(letter)
                word_letters.remove(letter)
        
        if not word_letters:
            messagebox.showinfo("Hangman", "Parabéns! Você venceu!")
            reset_game()
    else:
        lives_display.config(text=f"Vidas restantes: {lives}")
        lives -= 1
        
        if lives == 0:
            messagebox.showinfo("Hangman", f"Você perdeu! A palavra era '{word}'.")
            reset_game()

# Função para reiniciar o jogo
def reset_game():
    global word, word_letters, lives
    
    word = get_valid_word(paises)
    word_letters = set(word.upper())
    lives = 6
    lives_display.config(text=f"Vidas restantes: {lives}")
    
    for i in range(len(word)):
        word_display[i].set("-")

# Lista de países
paises = ["Brasil", "Argentina", "Chile", "Uruguai", "Paraguai"]

# Variáveis globais
word = get_valid_word(paises)
word_letters = set(word.upper())
lives = 6

# Criar janela
root = tk.Tk()
root.title("Hangman")

# Frame principal
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack()

# Palavra em exibição
word_display = [tk.StringVar() for _ in range(len(word))]
word_label = tk.Label(main_frame, text=" ".join("-" for _ in word), font=("Arial", 18))
word_label.pack()

# Input de letra
letter_input = tk.Entry(main_frame, font=("Arial", 14))
letter_input.pack()

# Botão de adivinhar
guess_button = tk.Button(main_frame, text="Adivinhar", command=check_letter)
guess_button.pack()

# Vidas restantes
lives_display = tk.Label(main_frame, text=f"Vidas restantes: {lives}", font=("Arial", 14))
lives_display.pack()

# Botão de reiniciar
restart_button = tk.Button(main_frame, text="Reiniciar", command=reset_game)
restart_button.pack()

# Iniciar o loop da interface gráfica
root.mainloop()

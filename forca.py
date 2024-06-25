import random
import string

from paises import paises

def get_valid_word(paises):
    paises = random.choice(paises)
    while '-' in paises or ' ' in paises:
        paises = random.choice(paises)
    return paises

def hangman():
    paises_aleatorio = get_valid_word(paises)
    word_letters = set(paises_aleatorio.upper())
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 5  

    while len(word_letters) > 0 and lives > 0:
        print('Você já usou essas letras:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in paises_aleatorio.upper()]
        print('Palavra atual:', ' '.join(word_list))

        user_letter = input('Adivinhe uma letra: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives -= 1  
                print('Letra não está no país')
        elif user_letter in used_letters:
            print('Você já usou essa letra. Tente novamente.')
        else:
            print('Letra inválida. Tente novamente.')

    if lives == 0:
        print('Você morreu, desculpe. A palavra era', paises_aleatorio)
    else:
        print('Você adivinhou a palavra', paises_aleatorio, '!!')

if __name__ == "__main__":
    hangman()

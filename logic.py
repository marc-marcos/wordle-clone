import random
from wordlist import WORDS
from colorama import Fore, Back, Style

def get_random_word():
    random_number = random.randint(1, len(WORDS)-1)
    return WORDS[random_number]

def word_correctness(correct_word, user_word):
    c = []
    for i in range(len(correct_word)):
        if user_word[i] == correct_word[i]:
            c.append('V')
        
        elif user_word[i] in correct_word:
            c.append('A')
        
        else:
            c.append('G')
    
    return c

def print_word_in_screen(correct_word, user_word):
    correct_word = correct_word.upper()
    user_word = user_word.upper()

    c = word_correctness(correct_word, user_word)
    for i in range(len(correct_word)):
        if c[i] == 'V':
            print(Style.BRIGHT + Fore.GREEN + correct_word[i], end=' ')
        
        elif c[i] == 'A':
            print(Fore.YELLOW + user_word[i], end=' ')
        
        else:
            print(Fore.WHITE + user_word[i], end=' ')
        
    print(Style.RESET_ALL)
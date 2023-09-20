import logic
from colorama import Fore

if __name__ == '__main__':
    while True:
        correct_word = logic.get_random_word()

        win = False
        while win == False:
            user_word = input('>> ')

            if (len(user_word) == len(correct_word)):
                logic.print_word_in_screen(correct_word, user_word)
            
            else:
                print(Fore.RED + 'The word must have 5 letters.' + Fore.RESET)

            if correct_word == user_word:
                print('You win!')
                break

            print()

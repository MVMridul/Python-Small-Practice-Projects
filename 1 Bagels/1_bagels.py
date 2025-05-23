#1. """Bagels, by Al Sweigart al@inventwithpython.com
#2. A deductive logic game where you must guess a number based on clues.
#3. View this code at https://nostarch.com/big-book-small-python-projects
#4. A version of this game is featured in the book "Invent Your Own
#5. Computer Games with Python" https://nostarch.com/inventwithpython
#6. Tags: short, game, puzzle"""

import random

num_digits = 3   # (!) try setting this to 1 - 10
max_guesses = 10 # (!) try setting this to 10 - 50


def main():
    print(''' Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(num_digits))

    while True:  # Main game loop
        # It stores the secret number the player needs to guess:
            secretNum = getSecretNum()
            print('I have thought up a number.')
            print('You have {} guesses to get it.'.format(max_guesses))
            
            numGuesses = 1
            while numGuesses <= max_guesses:
                guess = ''
                # Keep looping until player enters a valid guess:
                while len(guess) != num_digits or not guess.isdecimal():
                    print('Guess #{}: '.format(numGuesses))
                    guess = input('> ')
                    
                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses +=1
                
                if guess == secretNum:
                    break  # Player correct, so break out of the loop
                if numGuesses > max_guesses:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(secretNum))
                    
            # Asking if player wants to play again.
            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
    print('Thanks for playing !!!')
    
    
def getSecretNum():
    """Returns a string made up of num_digits unique random disigts."""
    numbers = list('0123456789')   # Creates a list of digits 0-9
    random.shuffle(numbers)       # shuffles them into radom order
    
    # Get the first num_digits in the list for secret number
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with Pico, Fermi, Bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it !!!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in correct place
            clues.append('Fermi')  
        elif guess[i] in secretNum:
            # a correct digit is in incorrect place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no corerct digits at all
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)
    
    
# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
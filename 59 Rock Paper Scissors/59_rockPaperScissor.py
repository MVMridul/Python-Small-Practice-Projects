"""Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
The classic hand game of luck.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, game"""

import random, time, sys

print('''Rock, Paper, Scissors Game
      - Rock beats Scissors
      - Paper beats Rock
      - Scissors beats Paper
      ''')
      
# These variables keep track of number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True:  # Main game loop
    while True:   # Keep asking till player enters R, P, S, or Q
        print('\n{} wins, {} Losses, {} Ties \n'.format(wins, losses, ties))
        print('Enter your move: (R)ock, (P)aper, (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thank you for Playing -- Game Over')
            sys.exit()
            
        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of: R P S or Q')
            
    # Display player's choice
    if playerMove == 'R':
        print('ROCK vs ...')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER vs ...')
        playerMove == 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS vs ...')
        playerMove = 'SCISSORS'
    
    # Counting to three for dramatic pause
    time.sleep(0.5)
    print('1 ...')
    time.sleep(0.5)
    print('2 ...')
    time.sleep(0.5)
    print('3 ...')
    time.sleep(0.25)
    
    # Display what the computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        compMove = 'ROCK'
    elif randomNumber == 2:
        compMove = 'PAPER'
    elif randomNumber == 3:
        compMove = 'SCISSORS'
    print(compMove)
    time.sleep(0.5)
    
    # Display and reconrd the win/loss/tie
    if playerMove == compMove:
        print('It\'s a tie')
        ties = ties + 1
    elif playerMove == 'ROCK' and compMove == 'SCISSORS':
        print('You Win')
        wins = wins + 1
    elif playerMove == 'PAPER' and compMove == 'ROCK':
        print('You Win')
        wins = wins + 1
    elif playerMove == 'SCISSORS' and compMove == 'PAPER':
        print('You Win')
        wins = wins + 1
    elif playerMove == 'ROCK' and compMove == 'PAPER':
        print('You Lose')
        losses = losses + 1
    elif playerMove == 'PAPER' and compMove == 'SCISSORS':
        print('You Lose')
        losses = losses + 1
    elif playerMove == 'SCISSORS' and compMove == 'ROCK':
        print('You Lose')
        losses = losses + 1
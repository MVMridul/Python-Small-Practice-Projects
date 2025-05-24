"""Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, card game"""

import random, sys

# Set up the constants:
hearts = chr(9829)   # Character 9829 is '♥'
diamonds = chr(9830) # Character 9830 is '♦'
spades = chr(9824)   # Character 9824 is '♠'
clubs = chr(9827)    # Character 9827 is '♣'
# (A list of chr codes is at https://inventwithpython.com/charactermap)
backside = 'backside'



            
def getBet(maxBet):
    """Ask player how much they want to bet for this round"""
    while True:   # keep asking player until they enter a valid amount
        print('How much do you bet? (1 - {}, or Quit)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing !!!')
            sys.exit()
            
        if not bet.isdecimal():
            continue  # if player didnot enter a number, ask again
            
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet   # player entered a valid bet
        
        
def getDeck():
    """Returns a list of (rank , suit) tuples for all 52 cards"""
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2,11):
            deck.append((str(rank), suit))  # add nuumbered card
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # add face and ace cards
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first 
    card if showDealerhand is False"""
    print()
    if showDealerHand:
        print('DEALER : ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER : ???')
        # hide the dealer's first card
        displayCards([backside] + dealerHand[1:])
        
    # show player's cards
    print('PLAYER : ', getHandValue(playerHand))
    displayCards(playerHand)
    
    
def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    numberofAces = 0
    
    # add the value for non-ace cards
    for card in cards:
        rank = card[0]   # card is a tuple like (rank, suit)
        if rank == 'A':
            numberofAces += 1
        elif rank in ('K', 'Q', 'J'):  # face cards are worth 10 points
            value += 10
        else:
            value += int(rank)  # numbered cards are worth their number
    
    # Add value for aces
    value += numberofAces  # add 1 per ace
    for i in range(numberofAces):
        # if another 10 can be added with busting, do so
        if value + 10 <= 21:
            value += 10
            
    return value


def displayCards(cards):
    """Dsiplay all cards in the card list"""
    rows = ['','','','','']  # the text to display on each row
    
    for i, card in enumerate(cards):
        rows[0] += '___'   # print top line of the card
        if card == backside:
            # print card's back side
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            # print card's front
            rank, suit = card  # the card is a tuple data structure
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
            
    # print rows on the sreen
    for row in rows:
        print(row)
        
        
def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down."""
    while True:   # keep looping until palyer make a valid move
        # determine what moves the player can make
        moves = ['(H)it', '(S)tand']
        
        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
            
        # get the player's move
        movePrompt = ', '.join(moves) + '>'
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move   # player has entered valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move   # player has entered valid move
        
        
        
        
print('''Blackjack, by Al Sweigart al@inventwithpython.com

Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.''')

money = 5000
while True:  # Main game loop
    # Check if player has run out of money
    if money <= 0:
        print('You are broke')
        print('Good thing you were not playing with real money')
        print('Thank you for playing')
        sys.exit() 
        
    # Let player enter their bet for this round:
    print('Money = ', money)
    bet = getBet(money)
        
    # Give player and dealer two cards from the deck each
    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]
        
    # Handle player actoins
    print('Bet =', bet)
    while True:     # keep looping until player stands or busts
        displayHands(playerHand, dealerHand, False)
        print()
            
        # check if player has bust
        if getHandValue(playerHand) > 21:
            break
            
        # get player's move, either H, S, or D
        move = getMove(playerHand, money-bet)
            
        # Handle player's action
        if move == 'D':
            # player is doubling down, they can inacrease their bet
            additionalBet = getBet(min(bet, (money-bet)))
            bet += additionalBet
            print('Bet increased to {}.'.format(bet))
            print('Bet = ', bet)
                
        if move in ('H', 'D'):
            # hit or doubling down takes another card
            newCard = deck.pop()
            rank, suit = newCard
            print('You drew a {} of {}.'.format(rank, suit))
            playerHand.append(newCard)
                
            if getHandValue(playerHand) > 21:
                # the player has busted
                continue
                
        if move in ('S', 'D'):
            # stand / doubling down stops the player's turn
            break
            
    # handle dealer's actions
    if getHandValue(playerHand) <= 21:
        while getHandValue(dealerHand) < 17:
            # dealer hits
            print('Dealer Hits ...')
            dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand,  False)
                
            if getHandValue(dealerHand) > 21:
                break   # dealer has busted
            input('Press Enter to continue ...')
            print('\n\n')
                
    # show final hands
    displayHands(playerHand, dealerHand, True)
        
    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)
    # handle whether player won, lost, or tied
    if dealerValue > 21:
        print('Dealerr busts!! You win ₹{} !'.format(bet))
        money += bet
    elif (playerValue > 21) or (playerValue < dealerValue):
        print('You lost !!!')
        money -= bet
    elif playerValue > dealerValue:
        print('You won ₹{} !'.format(bet))
        money += bet
    elif playerValue == dealerValue:
        print('It\'s a tie, the is returned to you.')
            
    input('Press Enter to continue ...')
    print('\n\n')        
        

# if the program is run (instead of imported), run the program
#if __name__ == '__main__':
#    main()        
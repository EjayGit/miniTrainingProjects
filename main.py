from game import Game
from deck import Deck
from hand import Hand
from money import Money
import sys

print('Welcome to Blackjack')
money = Money(5000)
while True:
    # check if player has run out of money
    if money.amount <= 0:
        print('It is good you are not playing with real money.')
        print("Thanks for playing")
        sys.exit()
    # Ask player to enter their bet
    print('Money: ', money.amount)
    bet = money.get_bet(money.amount)
    #get deck
    deck = Deck()
    deck.shuffle()
    # Give dealer and player 2 cards from deck
    playerHand = Hand()
    dealerHand = Hand(dealer=True)
    for i in range(2):
        playerHand.add_card(deck.deal())
        dealerHand.add_card(deck.deal())
    print("Bet:", bet)
    while True:
from deck import Deck
from cards import Player
import sys
import time
from hand_calculator import handType
from compare_results import compareResults


print "~~~BACCARAT~~~"
name = raw_input("What is your name? >>>")
player = Player(name)
PlayedBefore = ""
while (PlayedBefore != "Y") or (PlayedBefore != "y") or (PlayedBefore != "N") or (PlayedBefore != "n"):
    response = raw_input("Have you played Baccarat on this machine before? Y or N >>> ")
    PlayedBefore = str(response)
    if PlayedBefore == "n" or PlayedBefore == "N":
        print "\n The best hand is 3 of a kind. \n Next best hand is all face cards. \n The third best hand has a point value of 9. If your hand adds up to 16 your score is 6. 18 would be 8 etc. \n Make your bets and beat the dealer in this game of chance! \n"
        break
    if PlayedBefore == "Y" or PlayedBefore == "y":
        break
gameOver = False
deck = Deck().shuffle()

while gameOver == False:
    # Making Bets
    player.bet = raw_input(
        "You have {} coins. How many would you like to bet? >>> ".format(
            player.bank))
    player.bet = int(player.bet)
    if player.bet > player.bank:
        print "Not enough mulah, chump!"
        continue
    player.bank -= player.bet

    # Deals three cards to player and dealer

    playerCards = []
    dealerCards = []

    for i in range(0, 3):
        playerCards.append(deck.draw())
        dealerCards.append(deck.draw())

    # calculates type of hand and returns (type, id/cumulative id/points)

    playerHand = handType(playerCards)
    dealerHand = handType(dealerCards)

    print "\nYour hand is...\n"
    for card in playerCards:
        print card
    print "*" * 20

    # gets results in form of (winner, message)

    results = compareResults(playerHand, dealerHand, player)
    winner = results[0]
    message = results[1]

    print "The dealer's hand is...\n"
    for card in dealerCards:
        time.sleep(1)
        print card
    time.sleep(1)
    print "*" * 20
    print message
    print "\n"

    if player.bank == 0:
        print "Game Over"
        gameOver = True
    else:
        deck.refresh()

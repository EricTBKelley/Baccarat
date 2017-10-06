from deck import Deck
from cards import Player
import sys
import time
from hand_calculator import handType


print "~~~BACCARAT~~~"
name = raw_input("What is your name? >>> ")
player = Player(name)
gameOver = False
deck = Deck().shuffle()

while gameOver == False:
    #Making Bets
    bet = raw_input("You have {} coins. How many would you like to bet? >>> ".format(player.bank))
    bet = int(bet)
    if bet > player.bank:
        print "Not enough mulah, chump!"
        continue
    player.bank -= bet

    #Deals three cards to player and dealer

    playerCards = []
    dealerCards = []


    for i in range(0,3):
        playerCards.append(deck.draw())
        dealerCards.append(deck.draw())

    #calculates score

    playerHand = handType(playerCards)
    dealerHand = handType(dealerCards)

    #display results

    winner = ""
    reason = ""

    print "\nYour hand is...\n"
    for card in playerCards:
        print card
    print "*" * 20

    if playerHand[0] == "3kind":
        print "Three of a kind!"
        if dealerHand[0] == "3kind":
            if dealerHand[1] > playerHand[1]:
                winner = "dealer"
                reason = "The dealer has better 3 of a kind. You unlucky bastard..."
            else:
                winner = "player"
                reason = "You got a better 3 of a kind! HOLY CRAP, WINRAR!"
                player.bank += bet*5
        else:
            winner = "player"
            reason = "You got 3 of a kind! Wow! You don't completely suck!"
            player.bank += bet*5
    elif playerHand[0] == "allFace":
        print "All Face Cards"
        if dealerHand[0] == "allFace":
            winner = "dealer"
            reason = "Both you and the dealer got all face cards! They win, sucks..."
        if dealerHand[0] == "3kind":
            winner = "dealer"
            reason = "The dealer got 3 of a kind. hahahahahahahahaha"
        else:
            winner = "player"
            reason = "You got all face cards! Niceeeeeeee"
            player.bank += bet*3
    elif playerHand[0] == "points":
        print "{} points!".format(playerHand[1])
        time.sleep(1)
        print "\n"
        if dealerHand[0] == "3kind":
            winner = "dealer"
            reason = "The dealer got 3 of a kind!"
        elif dealerHand[0] == "allFace":
            winner = "dealer"
            reason = "The dealer got all face cards!"
        elif dealerHand[0] == "points":
            if dealerHand[1] > playerHand[1]:
                winner = "dealer"
                reason = "{} points. LOSER LOSER LOSER".format(dealerHand[1])
            elif dealerHand[1] == playerHand[1]:
                winner = "dealer"
                reason = "{} points!!!!!!!! you still lose :(".format(dealerHand[1])
            else:
                winner = "player"
                reason = "{} points! \n \n You win!... no dollars. this is a computer game with fictional currency. idiot. \n but here's some fake coins. whatever.".format(dealerHand[1])
                player.bank += bet*2


    print "The dealer's hand is...\n"
    for card in dealerCards:
        time.sleep(1)
        print card
    time.sleep(1)
    print "*" * 20
    print reason
    print "\n"


    if player.bank == 0:
        print "Game Over"
        gameOver = True
    else:
        deck.refresh()

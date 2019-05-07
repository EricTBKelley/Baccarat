import time


def compareResults(playerHand, dealerHand, player):
    if playerHand[0] == "3kind":
        print "Three of a kind!"
        if dealerHand[0] == "3kind":
            if dealerHand[1] > playerHand[1]:
                winner = "dealer"
                message = "The dealer has better 3 of a kind. Too bad.."
            else:
                winner = "player"
                message = "You got a better 3 of a kind! NOICE!"
                player.bank += player.bet * 5
        else:
            winner = "player"
            message = "You got 3 of a kind! Wow! Lucky!"
            player.bank += player.bet * 5
    elif playerHand[0] == "allFace":
        print "All Face Cards"
        if dealerHand[0] == "allFace":
            winner = "dealer"
            message = "Both you and the dealer got all face cards! Tie goes to the dealer..."
        if dealerHand[0] == "3kind":
            winner = "dealer"
            message = "But the dealer got 3 of a kind. That is so so unlikely and I'm sorry for your loss"
        else:
            winner = "player"
            message = "You got all face cards! Nice!"
            player.bank += player.bet * 3
    elif playerHand[0] == "points":
        print "{} points!".format(playerHand[1])
        time.sleep(1)
        print "\n"
        if dealerHand[0] == "3kind":
            winner = "dealer"
            message = "The dealer got 3 of a kind!"
        elif dealerHand[0] == "allFace":
            winner = "dealer"
            message = "The dealer got all face cards!"
        elif dealerHand[0] == "points":
            if dealerHand[1] > playerHand[1]:
                winner = "dealer"
                message = "{} points. Dealer wins.".format(dealerHand[1])
            elif dealerHand[1] == playerHand[1]:
                winner = "dealer"
                message = "{} points! Tie goes to the dealer".format(
                    dealerHand[1])
            else:
                winner = "player"
                message = "{} points! \n \n You win!".format(
                    dealerHand[1])
                player.bank += player.bet * 2
    return (winner, message)

import time


def compareResults(playerHand, dealerHand, player):
    if playerHand[0] == "3kind":
        print "Three of a kind!"
        if dealerHand[0] == "3kind":
            if dealerHand[1] > playerHand[1]:
                winner = "dealer"
                message = "The dealer has better 3 of a kind. You unlucky bastard..."
            else:
                winner = "player"
                message = "You got a better 3 of a kind! HOLY CRAP, WINRAR!"
                player.bank += player.bet * 5
        else:
            winner = "player"
            message = "You got 3 of a kind! Wow! You don't completely suck!"
            player.bank += player.bet * 5
    elif playerHand[0] == "allFace":
        print "All Face Cards"
        if dealerHand[0] == "allFace":
            winner = "dealer"
            message = "Both you and the dealer got all face cards! They win, sucks..."
        if dealerHand[0] == "3kind":
            winner = "dealer"
            message = "The dealer got 3 of a kind. hahahahahahahahaha"
        else:
            winner = "player"
            message = "You got all face cards! Niceeeeeeee"
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
                message = "{} points. LOSER LOSER LOSER".format(dealerHand[1])
            elif dealerHand[1] == playerHand[1]:
                winner = "dealer"
                message = "{} points!!!!!!!! you still lose :(".format(
                    dealerHand[1])
            else:
                winner = "player"
                message = "{} points! \n \n You win!... no dollars. this is a computer game with fictional currency. idiot. \n but here's some fake coins. whatever.".format(
                    dealerHand[1])
                player.bank += player.bet * 2
    return (winner, message)

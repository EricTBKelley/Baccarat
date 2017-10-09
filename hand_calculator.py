def calcScore(hand):
    total = 0
    for card in hand:
        total += card.value
    return total % 10


def handType(hand):
    if hand[0].id == hand[1].id == hand[2].id:
        typeOfHand = "3kind"
        number = hand[0].id
    elif hand[0].type == hand[1].type == hand[2].type == "face":
        typeOfHand = "allFace"
        number = hand[0].id + hand[1].id + hand[2].id
    else:
        typeOfHand = "points"
        number = calcScore(hand)
    return (typeOfHand, number)

from cards import Card
import random

class Deck(object):
    def __init__(self):
        self.nextIndex = 0
        self.cards = []
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
        numbers = [2,3,4,5,6,7,8,9,10,"Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for number in numbers:
                card = Card(suit, number)
                self.cards.append(card)
    def shuffle(self):
        for x in range(0,len(self.cards)):
            rand = random.randint(0,51)
            temp = self.cards[x]
            self.cards[x] = self.cards[rand]
            self.cards[rand] = temp
        return self
    def draw(self):
        card = self.cards[self.nextIndex]
        self.nextIndex += 1
        return card
    def refresh(self):
        self.shuffle()
        self.nextIndex = 0
        return self

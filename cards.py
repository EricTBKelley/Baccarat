class Card(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        if number == "Ace":
            self.type = "number"
            self.value = 1
            self.id = 14
        elif number == "Jack":
            self.type = "face"
            self.value = 0
            self.id = 11
        elif number == "Queen":
            self.type = "face"
            self.value = 0
            self.id = 12
        elif number == "King":
            self.type = "face"
            self.value = 0
            self.id = 13
        else:
            self.type = "number"
            self.value = number
            self.id = number
    def __str__(self):
        return "{} of {}".format(self.number, self.suit)

class Player(object):
    def __init__(self, name):
        self.name = name
        self.bank = 200

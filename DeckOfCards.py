from itertools import product
from random import shuffle



class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value




class Deck:

    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'Jack':
                value = 11
            elif rank == 'Queen':
                value = 12
            elif rank == 'King':
                value = 13
            else:
                rank.isdigit()
                value = int(rank)
            c = Card(suit=suit, rank=rank, points=value)
            cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    # == __eq__
    # != __ne__
    # >  __gt__
    # <  __lt__
    # >= __ge__
    # <= __le__

if __name__ == "__main__":
    suit = ['Diamod', 'Spade', 'Heart', 'Club']
    points = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']










    # print("p1",p1)
    # list1 = [p1,p2,p3]
    #
    # print(list1)
    # list1[0].address="cccccccccccccccccccccccc"
    #
    # print("p1",p1)
    # print("p4",p4)
    # print(p1 in list1)


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [
        None, None,
        "2", "3", "4", "5", "6", "7", "8", "9",
        "10", "Jack", "Queen", "King", "Ace"
    ]

    def __init__(self, v, s):
        """スート(マーク)も値も整数値です"""
        self.value = v
        self.suit = s

    # 特殊method less than
    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    # 特殊method greater than
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v

card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2)
print(card1 > card2)
print(card1)
print(card2)
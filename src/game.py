import random
from enum import Enum

LEFT_WINS = 1
RIGHT_WINS = -1
DRAW = 0


def compare(hand1, hand2):
    return hand1 > hand2


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __lt__(self, other):
        if self.value == other.value:
            return DRAW
        if self.value - other.value == 1 or self.value - other.value == -2:
            return RIGHT_WINS
        return LEFT_WINS


class RandomPlayer():
    def next_hand(self):
        r = random.random()
        if r > 0.66:
            return Hand.ROCK
        elif r > 0.33:
            return Hand.PAPER
        else:
            return Hand.SCISSORS


class Game():
    def play(self, player1, player2):
        for _ in range(10):
            hand1 = player1.next_hand()
            hand2 = player2.next_hand()
            winlose = compare(hand1, hand2)
            if winlose != DRAW:
                return winlose
        return DRAW

import pytest
from unittest.mock import MagicMock
from game import *


def test_game():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    player1.next_hand = MagicMock(return_value=Hand.ROCK)
    player2.next_hand = MagicMock(return_value=Hand.SCISSORS)
    game = Game()
    winlose = game.play(player1, player2)
    assert winlose == LEFT_WINS


def test_game_draw():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    player1.next_hand = MagicMock(return_value=Hand.ROCK)
    player2.next_hand = MagicMock(return_value=Hand.ROCK)
    game = Game()
    winlose = game.play(player1, player2)
    assert winlose == DRAW


def test_random_player1(mocker):
    mocker.patch('random.random', return_value=0.7)
    player = RandomPlayer()
    hand = player.next_hand()
    assert hand == Hand.ROCK


@pytest.mark.skip(reason='affects all random.random due to mock')
def test_random_player2():
    import random
    random.random = MagicMock(return_value=0.67)
    player = RandomPlayer()
    hand = player.next_hand()
    assert hand == Hand.ROCK


def test_random_player_statistically():
    player = RandomPlayer()
    hands = []
    rounds = 1000
    for _ in range(rounds):
        hands.append(player.next_hand())
    avg = rounds / 3
    err = rounds / 10
    assert hands.count(Hand.ROCK) > avg - \
        err and hands.count(Hand.ROCK) < avg + err

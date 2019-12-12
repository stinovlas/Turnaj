from Player import Player
from Player import Move


class TitForTat(Player):

    def __init__(self):
        self.last = Move.Cooperate

    def author_name(self):
        return "Tom"

    def next_move(self):
        return self.last

    def reward(self, result):
        self.last = result.opp_move

import random

from player import Move, Player


class Mirror(Player):
    """Mirror player.

    Start with ASafeWay.
    In following turns, choose randomly one of last 3 moves our opponent made.
    """

    def __init__(self):
        """We remember all our opponent moves."""
        self.opponent_moves = []

    def author_name(self):
        return "Honza"

    def next_move(self):
        """Choose randoly one of last 3 moves our opponent made."""
        if not self.opponent_moves:  # It's first round of the game, there has been no moves
            return Move.Cooperate
        else:
            last_moves = self.opponent_moves[-3:]  # We select last three moves from the list
            return random.choice(last_moves)

    def reward(self, result):
        """Record history of the game."""
        self.opponent_moves.append(result.opp_move)

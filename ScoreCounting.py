from Player import Move, Player


class ScoreCounting(Player):
    """ScoreCounting player.

    Start with Cooperate.
    In following turns, chooses Cooperate if he has score greater or equal to his opponent's.
    Otherwise chooses Betray.
    """

    def __init__(self):
        """We remember our overall scores."""
        self.my_score = 0
        self.opponent_score = 0

    def author_name(self):
        return "Honza"

    def next_move(self):
        """Choose betrayal if you are loosing. Otherwise cooperate."""
        if self.my_score < self.opponent_score:
            return Move.Betray
        else:
            return Move.Cooperate

    def reward(self, result):
        """Add score from the last round to overall scores."""
        self.my_score += result.get_my_score()
        self.opponent_score += result.get_opp_score()

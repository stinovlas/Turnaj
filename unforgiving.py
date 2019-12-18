from player import Move, Player


class Unforgiving(Player):
    """Unforgiving player.

    Until he has been betrayed, always cooperates.
    As soon as he is betrayed, he betrays back and never forgives.
    """

    def __init__(self):
        """We remember whether the opponent ever betrayed us."""
        self.was_betrayed = False

    def author_name(self):
        return "Honza"

    def next_move(self):
        """Cooperate unless you were betrayed in the past. Otherwise betray."""
        if self.was_betrayed:
            return Move.Betray
        else:
            return Move.Cooperate

    def reward(self, result):
        """If opponent ever betrays us, we remember that."""
        if result.opp_move == Move.Betray:
            self.was_betrayed = True

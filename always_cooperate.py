from player import Move, Player


class AlwaysCooperate(Player):
    def __init__(self):
        pass

    def author_name(self):
        return "Marketa"

    def next_move(self):
        return Move.Cooperate

    def reward(self, result):
        pass

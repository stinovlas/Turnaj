from Player import Move


class Result:
    rewards = ((6, 2, 2, 2), (0, 2, 8, 5), (0, 0, 10, 1), (0, 1, 18, 4))

    def __init__(self, move1: Move, move2: Move):
        """Class constructor, allows to get the previous move values through class attributes"""
        self.my_move = move1
        self.opp_move = move2

    def getmyscore(self):
        """Returns number of your scored point"""
        if self.my_move and self.opp_move is not None:
            return self.rewards[self.my_move.value[1]][self.opp_move.value[1]]
        else:
            print("Error, moves have not been defined")
            exit(1)

    def getoppscore(self):
        """Returns number of opponent's scored points"""
        if self.my_move and self.opp_move is not None:
            return self.rewards[self.opp_move.value[1]][self.my_move.value[1]]
        else:
            print("Error, moves have not been defined")
            exit(1)

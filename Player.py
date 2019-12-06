import abc
import enum


class Move(enum.Enum):
    SafeWay = "A", 0
    Betray = "B", 1
    Cooperate = "C", 2
    Deceive = "D", 3


class Player(abc.ABC):
    @abc.abstractmethod
    def author_name(self) -> str:
        """Returns author's name in a string"""

    @abc.abstractmethod
    def next_move(self) -> Move:
        """Returns next move as Move enum type"""

    @abc.abstractmethod
    def reward(self, res):
        """The current game progress is available through the Result object"""

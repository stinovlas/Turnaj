from Player import Move
import importlib
import sys


def pick_next():
    moves = (('A', 0), ('B', 1), ('C', 2), ('D', 3))
    print("Pick your next move:")
    pick = str(input())
    for move in moves:
        if move[0].lower() == pick.lower():
            return Move(move)

    print("pick options: A,B,C,D")
    return pick_next()


def print_result(res, sc1, sc2):
    print("Your move was: {}".format(res.opp_move.value[0]))
    print("Your opponent's move was: {}".format(res.my_move.value[0]))
    print("You scored {}".format(res.get_opp_score()), ", total: {}".format(sc2))
    print("Your opponent scored {}".format(res.get_my_score()), ", total: {}".format(sc1))
    print("--------------------------->")


def print_score(sc1, sc2):
    print("THE GAME HAS ENDED")
    print("--------------------------->")
    print("You scored in total {} points.".format(sc2))
    print("AI player scored in total {} points.".format(sc1))


def main():
    if 2 <= len(sys.argv) < 4:
        iterations = 1
        try:
            iterations = int(sys.argv[2])
        except IndexError:
            iterations = 1
        except ValueError:
            print("The second argument should be a number!")
            exit(1)
        if isinstance(sys.argv[1], str):
            try:
                name = sys.argv[1].split('.py')
                strategy_name = name[0]
                strategy1 = importlib.import_module(strategy_name)
                s1 = getattr(strategy1, strategy_name)()
                sc1 = 0
                sc2 = 0

                from Result import Result
                for i in range(iterations):
                    move1 = s1.next_move()
                    move2 = pick_next()
                    r1 = Result(move1, move2)
                    sc1 += r1.get_my_score()
                    sc2 += r1.get_opp_score()
                    print_result(r1, sc1, sc2)
                    s1.reward(r1)

                print_score(sc1, sc2)
            except IOError:
                print('An error occurred trying to read the file.')
            except ImportError:
                print("NO module found")
        else:
            print("First argument should be the name of your script")
    else:
        print("Argument Error")


if __name__ == "__main__":
    main()

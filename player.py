class Player:

    def __init__(self) -> None:
        self.number_of_wins = 0
        self.number_of_games_played = 0

    def move(self, state):
        raise NotImplementedError("Move needs to be implemented")


class Human(Player):

    def move(self, state):
        print(state)
        return [int(input("Pick a move number: "))]


class Agent(Player):
    pass
    # def move(self,state):

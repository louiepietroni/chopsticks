from player import Player
import numpy as np


class Game:
    move_change_dictionary = {
        1: lambda state: np.array([[0, 0], [state[0][0], 0]]),
        2: lambda state: np.array([[0, 0], [0, state[0][0]]]),
        3: lambda state: np.array([[0, 0], [state[0][1], 0]]),
        4: lambda state: np.array([[0, 0], [0, state[0][1]]]),
        5: lambda state: np.array([[-1, 1], [0, 0]]),
        6: lambda state: np.array([[-2, 2], [0, 0]]),
        7: lambda state: np.array([[-3, 3], [0, 0]]),
        8: lambda state: np.array([[-4, 4], [0, 0]]),
        9: lambda state: np.array([[1, -1], [0, 0]]),
        10: lambda state: np.array([[2, -2], [0, 0]]),
        11: lambda state: np.array([[3, -3], [0, 0]]),
        12: lambda state: np.array([[4, -4], [0, 0]])
    }

    def __init__(
        self, player1: Player, player2: Player, state=np.array([[1, 1], [1, 1]])
    ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.state = state


    def isvalid(self, move, change):
        new_state = self.state + change
        if move == 1:
            if self.state[0][0] == 0 or self.state[1][0] == 0:
                return False
        elif move == 2:
            if self.state[0][0] == 0 or self.state[1][1] == 0:
                return False
        elif move == 3:
            if self.state[0][1] == 0 or self.state[1][0] == 0:
                return False   
        elif move == 4:
            if self.state[0][1] == 0 or self.state[1][1] == 0:
                return False     
        elif (new_state[0] < 0).any() or not np.any(new_state[0] - np.flip(self.state[0])):
            return False 
        return True      


    def play(self):
        while True:
            self.play_single_move()
            if not np.any(self.state[0]):
                self.player1.number_of_games_played += 1
                self.player2.number_of_games_played += 1
                self.player2.number_of_wins += 1
                print("game is over")
                break
                

    def play_single_move(self):
        move_choices = self.player1.move(self.state)
        for move in move_choices:
            change = Game.move_change_dictionary[move](self.state)
            if self.isvalid(move, Game.move_change_dictionary[move](self.state)):
                self.state = np.mod(self.state + change, 5) 
                self.state = np.array([self.state[1],self.state[0]])
                self.player1, self.player2 = self.player2, self.player1
                return self
        print("Not a valid  move") 
        return self.play_single_move()

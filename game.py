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
        12: lambda state: np.array([[4, -4], [0, 0]]),
    }

    def __init__(
        self, player1: Player, player2: Player, state=np.array([[1, 1], [1, 1]])
    ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.state = state


    def isvalid(self, move, change):
        if 1 <= move <= 2:
            if self.state[0][0] == 0:
                return False
        
        if 3 <= move <= 4:
            if self.state[0][-1] == 0:
        
    
    def play(self):
        while self.state.sum()[0] != 0 and self.state.sum()[1] != 0:
            move_choices = self.player1.move()
            for move in move_choices:
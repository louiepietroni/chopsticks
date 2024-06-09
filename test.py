import numpy as np
from game import Game
from player import Player, Human
1
player1 = Human()
player2 = Human()
game = Game(player1, player2)
game.play()

# import numpy as np
# print(np.any([0,0]))
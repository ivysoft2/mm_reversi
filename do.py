# -*- coding: utf-8 -*-
from ReversiBoard import ReversiBoard
from Player import Player
from LerningMachine import LerningMachine

board = ReversiBoard()
board.show()

playerA = LerningMachine(board, 'W')
playerB = LerningMachine(board, 'B')

while(not board.is_game_end()):
    playerA.put()
    board.show()
    playerB.put()
    board.show()

board.show()
print('game end.')
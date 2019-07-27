# -*- coding: utf-8 -*-
from ReversiBoard import ReversiBoard
from Player import Player
from LerningMachine import LerningMachine

board = ReversiBoard()
board.show()

winACnt = 0
winBCnt = 0

A=''
B=''

while True:
    board = ReversiBoard()
    playerA = LerningMachine(board, 'W')
    playerB = LerningMachine(board, 'B')

    try:
        playerA._q.load()
    except:
        pass
    
    while(not board.is_game_end()):
        playerA.put()
        playerB.put()

    playerA._q.save()

    if(board.is_draw()):
        print('A:' + str(winACnt) + ' B:' + str(winBCnt) + ' draw!!!!')
    elif(board.is_win('W')):
        winACnt+=1
        A+='A'
        B=''
        print('A:' + str(winACnt) + ' B:' + str(winBCnt) + ' ' + A)
    else:
        winBCnt+=1
        A=''
        B+='B'
        print('A:' + str(winACnt) + ' B:' + str(winBCnt) + ' '+ B)
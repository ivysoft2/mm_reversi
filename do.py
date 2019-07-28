# -*- coding: utf-8 -*-
from ReversiBoard import ReversiBoard
from Player import Player
from LerningMachine import LerningMachine

board = ReversiBoard()
board.show()

winACnt = 0
winBCnt = 0
drawCnt = 0
totalCnt = 0

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
        drawCnt+=1
    elif(board.is_win('W')):
        winACnt+=1
    else:
        winBCnt+=1
    
    totalCnt += 1
    print('Total:' + str(totalCnt) + ' A:' + str(winACnt) + '(' + str(round(winACnt/totalCnt,2)*100) + '%) B:' +\
          str(winBCnt) + '(' + str(round(winBCnt/totalCnt,2)*100) + '%) draw:' +\
          str(drawCnt)+ '(' + str(round(drawCnt/totalCnt,2)*100) + '%)')
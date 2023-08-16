import msvcrt
import os

size = 4
board = [[i + j for i in range(1,size+1)] for j in range(0,size*size,4)]
board[size-1][size-1] = 0

def printBoard():
    for item in board:
        print(board.index(item))
        for j in item:
            if j < 10:
                print(' ',end='')
            print(j,end=" ")
        print()


printBoard()
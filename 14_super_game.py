import random
SIZE = 10
MINES = 5

board = [[0 for i in range(SIZE)] for j in range(SIZE)]
revealed = [[False for i in range(SIZE)] for j in range(SIZE)]


def placeMines():
    count = 0
    while count < MINES:
        x = random.randrange(0, SIZE)
        y = random.randrange(0, SIZE)
        if (board[x][y] != -1):
            board[x][y] = -1
            count += 1





def printBoard():
    print('   ', end='')
    for i in range(SIZE):
        print(i, ' ', end='', sep='')
    print()
    print('  ', end='')
    for i in range(SIZE):
        print('--', end='', sep='')
    print()
    for i in range(SIZE):
        print(i, '|', sep='', end='')
        for j in range(SIZE):
            if revealed[i][j]:
                if board[i][j] == -1:
                    print(' *', end='')
                elif board[i][j] == 1:
                    print('\033[34m ', board[i][j], '\033[0m', end='', sep='')
                elif board[i][j] == 2:
                    print('\033[34m ', board[i][j], '\033[0m', end='', sep='')
                elif board[i][j] == 3:
                    print('\033[32m ', board[i][j], '\033[0m', end='', sep='')
                elif board[i][j] == 4:
                    print('\033[33m ', board[i][j], '\033[0m', end='', sep='')
                elif board[i][j] == 5:
                    print('\033[30m ', board[i][j], '\033[0m', end='', sep='')
                else:
                    print(' ',board[i][j], end='', sep='')
            else:
                print(' .', end='')
        print()
    print('\n')


def countMines(x, y):
    count = 0
    if x > 0 and board[x-1][y] == -1:
        count += 1
    if x < SIZE - 1 and board[x+1][y] == -1:
        count += 1
    if y > 0 and board[x][y-1] == -1:
        count += 1
    if y < SIZE-1 and board[x][y+1] == -1:
        count += 1
    if y < SIZE-1 and board[x][y+1] == -1:
        count += 1
    if x > 0 and y > 0 and board[x-1][y-1] == -1:
        count += 1
    if x > 0 and y < SIZE - 1 and board[x-1][y+1] == -1:
        count += 1
    if x < SIZE - 1 and y > 0 and board[x+1][y-1] == -1:
        count += 1
    if x < SIZE - 1 and y < SIZE - 1 and board[x+1][y+1] == -1:
        count += 1
    return count


def reveal(x, y):
    if board[x][y] == -1:
        printBoard()
        print('Game over')
        return False
    elif not revealed[x][y]:
        mines = countMines(x, y)
        board[x][y] = mines
        revealed[x][y] = True
        if mines == 0:
            if x > 0:
                reveal(x-1, y)
            if x < SIZE-1:
                reveal(x+1, y)
            if y > 0:
                reveal(x, y-1)
            if y < SIZE - 1:
                reveal(x, y+1)
            if x > 0 and y < SIZE - 1:
                reveal(x-1, y+1)
            if x > 0 and y > 0:
                reveal(x-1, y-1)
            if x < SIZE-1 and y > 0:
                reveal(x+1, y-1)
            if x < SIZE-1 and y < SIZE - 1:
                reveal(x+1, y+1)

def checkWin():
    count = 0 
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] != -1 and revealed[i][j]:
                count+=1
    return count == SIZE*SIZE*MINES

def game():
    placeMines()
    while True:
        x,y = map(int,input("enter ").split())
        if reveal(x,y) == False:
            break
        printBoard()
        if checkWin():
            print("Congratulation")
        
game()
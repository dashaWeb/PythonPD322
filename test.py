

# import msvcrt
# import os
# list = [[i+j for i in range(1,5)] for j in range(0,13,4)]
# def printList():
#     for i in list:
#         for j in i:
#             print(j,end='\t')
#         print()
# up,left,down,right = 72,75,77,80
# while True:
#     os.system('cls||clear')
#     printList()
#     pressedKey = msvcrt.getch()
#     if ord(pressedKey) == left:
#         print('Left')


# while True:
#     pressedKey = msvcrt.getch()
#     if str(pressedKey) == 'q':    
#         print("Q was pressed")
#     elif str(pressedKey) == 'x':    
#         sys.exit()
#     else:
#         print("Key Pressed:" + str(pressedKey))


import random




def create_board(rows, cols, num_mines):

    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    mines = []

    while len(mines) < num_mines:

        row = random.randint(0, rows - 1)

        col = random.randint(0, cols - 1)

        if (row, col) not in mines:

            mines.append((row, col))

            board[row][col] = '*'

    return board, mines




def count_adjacent_mines(board, row, col):

    count = 0

    for r in range(max(0, row - 1), min(row + 2, len(board))):

        for c in range(max(0, col - 1), min(col + 2, len(board[0]))):

            if board[r][c] == '*':

                count += 1

    return count




def reveal_empty_cells(board, visible_board, row, col):

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visible_board[row][col] != ' ':

        return




    visible_board[row][col] = str(count_adjacent_mines(board, row, col))

    if visible_board[row][col] == '0':

        for r in range(max(0, row - 1), min(row + 2, len(board))):

            for c in range(max(0, col - 1), min(col + 2, len(board[0]))):

                reveal_empty_cells(board, visible_board, r, c)




def print_board(board):

    cols = len(board[0])

    horizontal_line = '   ' + '+---' * cols + '+'

    print('     ' + '   '.join(str(i) for i in range(cols)))

    print(horizontal_line)

    for i, row in enumerate(board):

        print(f' {i} |', end='')

        for cell in row:

            print(f' {cell} |', end='')

        print('\n' + horizontal_line)




def play_game(rows, cols, num_mines):

    board, mines = create_board(rows, cols, num_mines)

    visible_board = [[' ' for _ in range(cols)] for _ in range(rows)]

    game_over = False




    while not game_over:

        print_board(visible_board)




        print("Enter the coordinates (row, col):")

        row = int(input("Row: "))

        col = int(input("Col: "))




        if (row, col) in mines:

            print("Game over! You hit a mine!")

            game_over = True

        else:

            reveal_empty_cells(board, visible_board, row, col)

            if all(all(cell != ' ' for cell in row) for row in visible_board):

                print("Congratulations! You won!")

                game_over = True




    # Відображення мін після закінчення гри

    for row, col in mines:

        visible_board[row][col] = '*'




    print("Final board:")

    print_board(visible_board)




def run_game():

    while True:

        print("Welcome to Minesweeper!")

        print("Select difficulty:")

        print("1. Easy (5x5, 5 mines)")

        print("2. Medium (7x7, 10 mines)")

        print("3. Hard (12x12, 20 mines)")

        print("4. Quit")

        choice = input("Enter your choice: ")




        if choice == '1':

            play_game(5, 5, 5)

        elif choice == '2':

            play_game(7, 7, 10)

        elif choice == '3':

            play_game(12, 12, 20)

        elif choice == '4':

            break

        else:

            print("Invalid choice. Please try again.")




run_game()
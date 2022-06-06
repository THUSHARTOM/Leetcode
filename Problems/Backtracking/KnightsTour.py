# Task is to route a knight in a chess board so that it visits all boxes

# chessboard size
from sqlalchemy import false, true


n = 8


def isSafe(x, y, board):
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False


def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def solveKT(n):

    # initialise Board
    board = [[-1 for i in range(n)]for i in range(n)]
    print(board[7][4])
    # move_x is the next move in x cordinate
    # move_y is the next move in y cordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Initial move
    board[0][0] = 0

    # step counter
    pos = 1

    # check if sol exist or not
    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        printSolution(n, board)


def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    if(pos == n**2):
        return True

    for i in range(8):

        new_x = int(curr_x + move_x[i])
        new_y = int(curr_y + move_y[i])
        if(isSafe(new_x, new_y, board)):
            print(new_x, new_y)
            board[new_x][new_y] = int(pos)
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True

            board[new_x][new_y] = -1
    return False


# Driver
if __name__ == "__main__":
    solveKT(n)

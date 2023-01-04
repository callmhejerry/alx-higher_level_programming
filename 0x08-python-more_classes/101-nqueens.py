#!/usr/bin/python3
from sys import argv

if len(argv) - 1 != 1:
    print("Usage: nqueens N")
    exit(1)

if type(int(argv[1])) is not int:
    print("N must be a number")
    exit(1)

if int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(argv[1])

def getBoard(size):
    board = [[0 for col in range(size)] for row in range(size)]
    return board

def check_left_dia(board, row, col):
    if row < 0 or col < 0:
        return True
    if board[row][col] == 1:
        return False
    return check_left_dia(board, row - 1, col - 1)

def check_right_dia(board, row, col):
    if row < 0 or col >= len(board):
        return True
    if board[row][col] == 1:
        return False
    return check_right_dia(board, row - 1, col + 1)

def isSafe(board, row, col):
    for r in range(row):
        if board[r][col] == 1:
            return False
    if not check_left_dia(board, row - 1, col - 1):
        return False

    if not check_right_dia(board, row - 1, col + 1):
        return False

    return True

def print_board(board):
    print("-------------------")
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                print("X", end=" ")
            else:
                print("O", end= " ")
        print()
    print("-------------------")


def print_matrix(matrix):
    for row in matrix:
        print(row)

def place_queen(board, cell):
    board[0][cell] = 1
    placement = [[0, cell]]
    for row in range(1, len(board)):
        for col in range(len(board)):
            if isSafe(board, row, col):
                board[row][col] = 1
                print_board(board)
                placement.append([row, col])
                break
    print(placement)


def back_track(board, res, inner_soln, row=0):
    if row >= len(board):
        return True
    for col in range(len(board[row])):
        if isSafe(board, row, col):
            board[row][col] = 1
            if back_track(board, res, inner_soln, row + 1):
                inner_soln.append([row, col])
                board[row][col] = 0
                if row != 0:
                    return True
                else:
                    res.append(inner_soln)
                    inner_soln = []
                    continue
            else:
                board[row][col] = 0
        else:
            continue    
    return False

def soln(n):
    inner_soln = []
    res = []
    board = getBoard(n)
    back_track(board, res, inner_soln)
    print_matrix(res)

if __name__ == "__main__":
    soln(n)
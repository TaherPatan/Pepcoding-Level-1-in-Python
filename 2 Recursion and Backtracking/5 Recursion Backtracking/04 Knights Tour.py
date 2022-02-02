def displayBoard(chess):
    for i in range(len(chess)):
        for j in range(len(chess)):
            print(chess[i][j], end=' ')
        print()
    print()


def printKnightsTour(chess, n, row, col, upcomingMove):
    if not (-1 < row < n and -1 < col < n and chess[row][col] == 0):
        return
    if upcomingMove == n * n:
        chess[row][col] = upcomingMove
        displayBoard(chess)
        chess[row][col] = 0
        return
    chess[row][col] = upcomingMove
    printKnightsTour(chess, n, row - 2, col + 1, upcomingMove + 1)
    printKnightsTour(chess, n, row - 1, col + 2, upcomingMove + 1)
    printKnightsTour(chess, n, row + 1, col + 2, upcomingMove + 1)
    printKnightsTour(chess, n, row + 2, col + 1, upcomingMove + 1)
    printKnightsTour(chess, n, row + 2, col - 1, upcomingMove + 1)
    printKnightsTour(chess, n, row + 1, col - 2, upcomingMove + 1)
    printKnightsTour(chess, n, row - 1, col - 2, upcomingMove + 1)
    printKnightsTour(chess, n, row - 2, col - 1, upcomingMove + 1)
    chess[row][col] = 0


if __name__ == '__main__':
    n = int(input())
    chess = [[0 for _ in range(n)] for _ in range(n)]
    row = int(input())
    col = int(input())
    printKnightsTour(chess, n, row, col, 1)

def isitsafe(chess, row, col):
    for i in range(row - 1, -1, -1):
        if chess[i][col]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(chess))):
        if chess[i][j]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if chess[i][j]:
            return False
    return True

def printnqueens(chess, asf, row):
    if row == len(chess):
        print(f'{asf}.')
        return
    for col in range(len(chess)):
        if isitsafe(chess, row, col):
            chess[row][col] = True
            printnqueens(chess, f'{asf}{row}-{col}, ', row + 1)
            chess[row][col] = False


if __name__ == '__main__':
    n = int(input())
    chess = [[False for _ in range(n)] for _ in range(n)]
    printnqueens(chess, "", 0)

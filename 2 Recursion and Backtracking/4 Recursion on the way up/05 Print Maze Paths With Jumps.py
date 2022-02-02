def printMazePaths(sr, sc, dr, dc, asf):
    if sr > dr or sc > dc:
        return
    elif sr == dr and sc == dc:
        print(asf)
        return
    for jump in range(1, dc - sc + 1):
        printMazePaths(sr, sc + jump, dr, dc, asf + 'h' + str(jump))
    for jump in range(1, dr - sr + 1):
        printMazePaths(sr + jump, sc, dr, dc, asf + 'v' + str(jump))
    for jump in range(1, max(dr - sr + 1, dc - sc + 1)):
        printMazePaths(sr + jump, sc + jump, dr, dc, asf + 'd' + str(jump))


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    printMazePaths(0, 0, n - 1, m - 1, "")

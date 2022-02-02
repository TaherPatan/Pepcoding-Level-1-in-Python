def printMazePaths(sr, sc, dr, dc, asf):
    if sr > dr or sc > dc:
        return
    elif sr == dr and sc == dc:
        print(asf)
        return
    printMazePaths(sr, sc + 1, dr, dc, asf + 'h')
    printMazePaths(sr + 1, sc, dr, dc, asf + 'v')


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    printMazePaths(0, 0, n - 1, m - 1, "")

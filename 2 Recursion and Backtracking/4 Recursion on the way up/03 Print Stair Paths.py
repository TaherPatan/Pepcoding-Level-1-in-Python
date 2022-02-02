def printStairPaths(ques, asf):
    if ques == 0:
        print(asf)
    elif ques < 0:
        return
    printStairPaths(ques - 1, asf + '1')
    printStairPaths(ques - 2, asf + '2')
    printStairPaths(ques - 3, asf + '3')


if __name__ == '__main__':
    ques = int(input())
    printStairPaths(ques, "")

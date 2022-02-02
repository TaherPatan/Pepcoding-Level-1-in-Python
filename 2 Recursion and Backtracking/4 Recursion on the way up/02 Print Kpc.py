def printKPC(s, ques):
    if len(s) == 0:
        print(ques)
        return
    alphabets = ('.;', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tu', 'vwx', 'yz')
    num, ans = s[0], s[1:]
    for i in alphabets[int(num)]:
        printKPC(ans, ques + i)


if __name__ == '__main__':
    s = input()
    printKPC(s, '')

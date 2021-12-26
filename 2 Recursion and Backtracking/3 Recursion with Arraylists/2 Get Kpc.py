def getKPC(s):
    if len(s) == 0:
        return ['']
    alphabets = ('.;', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tu', 'vwx', 'yz')
    ans1, num1 = getKPC(s[1:]), int(s[0])
    final_ans = [letters + words for letters in alphabets[num1] for words in ans1]
    return final_ans


if __name__ == '__main__':
    s = input()
    ans = getKPC(s)
    print("[" + ', '.join(ans) + "]")

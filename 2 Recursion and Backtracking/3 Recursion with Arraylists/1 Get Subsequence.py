def getSS(s):
    if len(s) == 0:
        return ['']
    ch = s[0]
    ros = s[1:]
    rres = getSS(ros)
    mres = rres.copy()
    for i in rres:
        mres.append(ch + i)
    return mres


if __name__ == '__main__':
    s = input()
    ans = getSS(s)
    print("[" + ', '.join(ans) + "]")

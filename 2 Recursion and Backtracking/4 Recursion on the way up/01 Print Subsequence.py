def pss(ques, asf):
    if len(ques) == 0:
        print(asf)
        return
    ch = ques[0]
    roq = ques[1:]
    pss(roq, asf + ch)
    pss(roq, asf)


if __name__ == '__main__':
    s = input()
    pss(s, '')

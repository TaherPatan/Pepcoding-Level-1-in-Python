def print_permutations(ques, asf):
    if len(ques) == 0:
        print(asf)
        return
    for i in range(len(ques)):
        ch = ques[i]
        ros = ques[0:i] + ques[i + 1:]
        print_permutations(ros, asf + ch)


if __name__ == '__main__':
    s = input()
    print_permutations(s, '')

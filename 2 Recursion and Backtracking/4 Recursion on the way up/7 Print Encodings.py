def print_encodings(ques, asf):
    if len(ques) == 0:
        print(asf)
        return
    if ques[0] == '0':
        return
    print_encodings(ques[1:], asf + chr(ord('a') + int(ques[0]) - 1))
    if len(ques) >= 2 and 1 <= int(ques[0:2]) <= 26:
        print_encodings(ques[2:], asf + chr(ord('a') + int(ques[0:2]) - 1))


if __name__ == '__main__':
    s = input()
    print_encodings(s, '')

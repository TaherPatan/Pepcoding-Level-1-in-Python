def balanced_brackets(string):
    lst = []
    for s in string:
        if s in '([{':
            lst.append(s)
        elif s == ')':
            if not lst or lst[-1] != '(':
                return 'false'
            lst.pop()
        elif s == '}':
            if not lst or lst[-1] != '{':
                return 'false'
            lst.pop()
        elif s == ']':
            if not lst or lst[-1] != '[':
                return 'false'
            lst.pop()
    if not lst:
        return 'true'
    else:
        return 'false'


if __name__ == "__main__":
    string = input()
    print(balanced_brackets(string))

def duplicate_brackets(string):
    stack = []
    for i in string:
        if i != ')':
            stack.append(i)
        else:
            if stack[-1] == '(':
                return 'true'
            while stack[-1] != '(':
                stack.pop()
            stack.pop()
    return 'false'


if __name__ == "__main__":
    s = input()
    print(duplicate_brackets(s))

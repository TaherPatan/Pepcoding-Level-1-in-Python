def find_pattern(pattern):
    stack = [1]
    dig = ''
    num = 2
    for i in pattern:
        if i == 'i':
            while stack:
                dig = dig + str(stack.pop())
        stack.append(num)
        num += 1
    while stack:
        dig = dig + str(stack.pop())
    return dig


if __name__ == '__main__':
    num = input()
    print(find_pattern(num))

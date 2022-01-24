def findCelebrity(arr):
    stack = [i for i in range(len(arr))]
    while len(stack) != 1:
        element_1, element_2 = stack.pop(), stack.pop()
        if arr[element_1][element_2] == '1':
            stack.append(element_2)
        else:
            stack.append(element_1)
    for i in range(len(arr)):
        if i != stack[-1]:
            if arr[i][stack[-1]] == '0' or arr[stack[-1]][i] == '1':
                print('none')
                return
    print(stack[-1])


if __name__ == '__main__':
    n = int(input())
    arr = [input() for _ in range(n)]
    findCelebrity(arr)

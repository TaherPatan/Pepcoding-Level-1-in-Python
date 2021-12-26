def solution(al):
    for i in range(len(al) - 1, -1, -1):
        flag = True
        for j in range(2, int(al[i] ** 1 / 2) + 1):
            if al[i] % j == 0:
                flag = False
                break
        if flag:
            al.pop(i)


if __name__ == '__main__':
    n = int(input())
    al = []
    al = list(map(int, input().split()))
    solution(al)
    print(al)

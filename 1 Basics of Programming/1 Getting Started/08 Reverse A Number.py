def reverse_digs(num):
    num = str(abs(num))
    for i in range(len(num) - 1, -1, -1):
        print(num[i])


n = int(input())
reverse_digs(n)

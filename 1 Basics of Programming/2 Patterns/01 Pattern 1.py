def print_stars(num):
    for i in range(1, num + 1):
        for j in range(0, i):
            print('*\t', end='')
        print()


num1 = int(input())
print_stars(num1)
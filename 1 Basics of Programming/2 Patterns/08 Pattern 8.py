def print_stars(num1):
    for j in range(1, num1 + 1):
        print('*', end='\t')


def print_space(num2):
    for k in range(1, num2 + 1):
        print('	', end='')


def print_rows(num3):
    for i in range(num3 - 1, -1, -1):
        print_space(i)
        print_stars(1)
        print()


num4 = int(input())
print_rows(num4)

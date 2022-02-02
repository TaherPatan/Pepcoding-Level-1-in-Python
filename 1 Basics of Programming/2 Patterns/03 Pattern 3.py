def print_stars(num1):
    for j in range(0, num1):
        print('*', end='\t')


def print_space(num2):
    for k in range(num2):
        print('	', end='')


def print_rows(num3):
    for i in range(1, num3 + 1):
        print_space(num3 - i)
        print_stars(i)
        print()


num4 = int(input())
print_rows(num4)

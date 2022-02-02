def print_stars(num1):
    for j in range(0, num1):
        print('*', end='\t')


def no_of_rows(num2):
    for i in range(num2, 0, -1):
        print_stars(i)
        print()


num3 = int(input())
no_of_rows(num3)

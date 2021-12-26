def print_stars(num1):
    for j in range(1, num1 + 1):
        print('*', end='\t')


def print_space(num2):
    for k in range(1, num2 + 1):
        print('	', end='')


def print_rows(num3):
    os = num3 // 2
    ins = -1
    for i in range(1, num3 + 1):
        print_space(os)
        print_stars(1)
        print_space(ins)
        if i != 1 and i != num3:
            print_stars(1)
        print()
        if i <= num3 // 2:
            os -= 1
            ins += 2
        else:
            os += 1
            ins -= 2


num4 = int(input())
print_rows(num4)

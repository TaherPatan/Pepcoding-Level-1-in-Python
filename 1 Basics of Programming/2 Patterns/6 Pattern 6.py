def print_stars(num1):
    for j in range(1, num1 + 1):
        print('*', end='\t')


def print_space(num2):
    for k in range(1, num2 + 1):
        print('	', end='')


def print_rows(num3):
    sp = 1
    st = num3 // 2 + 1
    for i in range(1, num3 + 1):
        print_stars(st)
        print_space(sp)
        print_stars(st)
        print()
        if i <= num3 // 2:
            st -= 1
            sp += 2
        else:
            st += 1
            sp -= 2


num4 = int(input())
print_rows(num4)

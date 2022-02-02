def print_rows(num3):
    for i in range(1, num3 + 1):
        for j in range(1, num3 + 1):
            if i + j == num3 + 1 or i == j:
                print('*\t', end='')
            else:
                print('\t', end='')
        print()


num4 = int(input())
print_rows(num4)

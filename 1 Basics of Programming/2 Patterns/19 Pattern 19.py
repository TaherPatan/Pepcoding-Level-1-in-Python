def print_num(num):
    for i in range(1, num + 1):
        for j in range(1, num // 2 + 1):
            if (j <= num // 2 and i == 1) or (j <= num // 2 and i == num // 2 + 1) or (j == 1 and num // 2 + 1 < i):
                print('*', end='\t')
            else:
                print('\t', end='')
        print('*', end='\t')
        for k in range(1, num // 2 + 1):
            if (k < num // 2 and i <= num // 2) or (k <= num // 2 + 1 and i > num // 2 + 1 and i != num):
                print('\t', end='')
            else:
                print('*', end='\t')
        print()


num4 = int(input())
print_num(num4)

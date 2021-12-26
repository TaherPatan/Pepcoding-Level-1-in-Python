def print_num(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if j == 1 or j == num:
                print('*', end='\t')
            elif num // 2 < i and (i == j or i + j == num + 1):
                print('*', end='\t')
            else:
                print('\t', end='')
        print()


num4 = int(input())
print_num(num4)

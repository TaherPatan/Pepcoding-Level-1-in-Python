def print_num(num):
    sp = num // 2
    st = 1
    for i in range(1, num + 1):
        for j in range(sp):
            if i == num // 2 + 1:
                print('*', end='\t')
            else:
                print('\t', end='')
        for k in range(st):
            print('*', end='\t')
        print()
        if i <= num // 2:
            st += 1
        elif i >= num // 2:
            st -= 1


num4 = int(input())
print_num(num4)

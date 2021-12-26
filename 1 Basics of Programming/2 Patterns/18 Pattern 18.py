def print_num(num):
    st = num
    sp = 0
    for i in range(1, num + 1):
        for j in range(sp):
            print('\t', end='')
        for k in range(1, st + 1):
            if 1 < i <= num // 2 and 1 < k < st:
                print('\t', end='')
            else:
                print('*', end='\t')
        for j in range(sp):
            print('\t', end='')
        if i <= num // 2:
            st -= 2
            sp += 1
        else:
            st += 2
            sp -= 1
        print()


num4 = int(input())
print_num(num4)

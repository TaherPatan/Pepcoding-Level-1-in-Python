def print_num(num):
    sp = num // 2
    st = 1
    val = 1
    for i in range(1, num + 1):
        for j in range(1, sp + 1):
            print('\t', end='')
        cval = val
        for k in range(1, st + 1):
            print(cval, end='\t')
            if k <= st // 2:
                cval += 1
            else:
                cval -= 1
        if i <= num //2:
            sp -= 1
            st += 2
            val += 1
        else:
            sp += 1
            st -= 2
            val -= 1
        print()


num4 = int(input())
print_num(num4)

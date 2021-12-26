def print_num(num):
    for i in range(num):
        icj = 1
        for j in range(i + 1):
            print(icj, end='\t')
            icjp1 = icj * (i - j) // (j + 1)
            icj = icjp1
        print()


num4 = int(input())
print_num(num4)

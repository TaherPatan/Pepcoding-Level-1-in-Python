def print_num(num):
    a = 0
    b = 1
    c = a + b
    print(a)
    for i in range(2, num + 1):
        for j in range(i):
            print(c, end='\t')
            c = a + b
            a = b
            b = c
        print()


num4 = int(input())
print_num(num4)

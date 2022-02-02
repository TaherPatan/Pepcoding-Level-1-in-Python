def subtraction(base, num2, num1):
    rv = 0
    p = 0
    c = 0
    while num1 > 0:
        num1_dig = num1 % 10 + c
        num1 //= 10
        num2_dig = num2 % 10
        num2 //= 10
        if num1_dig - num2_dig >= 0:
            c = 0
            rv += (num1_dig - num2_dig) * 10 ** p
            p += 1
        else:
            c = -1
            rv += (num1_dig + base - num2_dig) * 10 ** p
            p += 1
    return rv


if __name__ == '__main__':
    b = int(input())
    n1 = int(input())
    n2 = int(input())
    print(subtraction(b, n1, n2))

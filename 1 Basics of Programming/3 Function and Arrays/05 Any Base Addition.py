def addition(base, num1, num2):
    rv = 0
    c = 0
    p = 0
    while num1 > 0 or num2 > 0 or c > 0:
        num1_dig = num1 % 10
        num1 //= 10
        num2_dig = num2 % 10
        num2 //= 10
        sum_of_dig_carry = num1_dig + num2_dig + c
        c = sum_of_dig_carry // base
        sum_of_dig_carry = sum_of_dig_carry % base
        rv += sum_of_dig_carry * 10 ** p
        p += 1
    return rv


if __name__ == '__main__':
    b = int(input())
    n1 = int(input())
    n2 = int(input())
    print(addition(b, n1, n2))


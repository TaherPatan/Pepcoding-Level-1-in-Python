def addition(num1, num2, base):
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


def single_digit_multiplication(num, dig, base):
    c = 0
    p = 0
    rv = 0
    while num > 0 or c > 0:
        mul = (num % 10 * dig) + c
        num //= 10
        c = mul // base
        mul = mul % base
        rv += mul * 10 ** p
        p += 1
    return rv


def multiplication(num1, num2, base):
    p = 0
    rv = 0
    while num1 > 0:
        d = num1 % 10
        num1 //= 10
        result = single_digit_multiplication(num2, d, base)
        rv = addition(rv, result * 10 ** p, base)
        p += 1
    return rv


b = int(input())
n1 = int(input())
n2 = int(input())
print(multiplication(n1, n2, b))
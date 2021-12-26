def gcd(n1, n2):
    while n1 % n2 != 0:
        rem = n1 % n2
        n1 = n2
        n2 = rem
    return rem


def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)


a, b = int(input()), int(input())
print(gcd(a, b))
print(lcm(a, b))

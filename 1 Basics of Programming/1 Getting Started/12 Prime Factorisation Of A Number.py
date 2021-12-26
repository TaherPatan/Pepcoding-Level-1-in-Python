def print_prime_factors(num1):
    i = 2
    while i * i <= num1:
        while num1 % i == 0:
            num1 //= i
            print(i, end=' ')
        i += 1
    if i != 1:
        print(num1)


num = int(input())
print_prime_factors(num)

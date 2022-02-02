def print_all_primes(start, end):
    for j in range(start, end + 1):
        prime = True
        if j == 2:
            print(2)
        else:
            for i in range(2, int(j ** 0.5 + 1)):
                if j % i == 0:
                    prime = False
                    break
            if prime:
                print(j)


low = int(input())
high = int(input())
print_all_primes(low, high)

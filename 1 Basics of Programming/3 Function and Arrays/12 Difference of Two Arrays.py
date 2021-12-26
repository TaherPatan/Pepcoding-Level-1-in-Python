def subtraction(one, two):
    sum_arr = [0] * max(len(one), len(two))
    i = len(one) - 1
    j = len(two) - 1
    k = len(sum_arr) - 1
    b = 0
    while k >= 0:
        d = two[j] - b
        if i >= 0:
            d = d - one[i]
        if d >= 0:
            b = 0
        elif d < 0:
            b = 1
            d = 10 + d
        sum_arr[k] = d
        i -= 1
        j -= 1
        k -= 1
    return sum_arr


n1 = int(input())
a1 = [int(input()) for i in range(n1)]
n2 = int(input())
a2 = [int(input()) for i in range(n2)]
subtracted = subtraction(a1, a2)
while True:
    if subtracted[0] != 0:
        break
    subtracted.pop(0)
for i in subtracted:
    print(i)

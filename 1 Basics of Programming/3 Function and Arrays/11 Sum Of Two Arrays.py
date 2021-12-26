def addition(one, two):
    sum_arr = [0] * max(len(one), len(two))
    i = len(one) - 1
    j = len(two) - 1
    k = len(sum_arr) - 1
    c = 0
    while k >= 0 or c > 0:
        d = c
        if i >= 0:
            d = d + one[i]
        if j >= 0:
            d = d + two[j]
        c = d // 10
        d = d % 10
        sum_arr[k] = d
        i -= 1
        j -= 1
        k -= 1
    return sum_arr


n1 = int(input())
a1 = [int(input()) for i in range(n1)]
n2 = int(input())
a2 = [int(input()) for i in range(n2)]
added = addition(a1, a2)
for i in added:
    print(i)

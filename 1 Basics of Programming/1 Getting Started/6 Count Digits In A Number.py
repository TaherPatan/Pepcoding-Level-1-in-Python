def count_dig(num):
    num = str(abs(num))
    return len(num)


n = int(input())
print(count_dig(n))

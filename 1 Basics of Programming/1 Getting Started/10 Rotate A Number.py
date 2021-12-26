def rotate(num, k):
    dig_count = len(str(num))
    x = num
    if k > 0:
        k = k % dig_count
    else:
        k = -(k % dig_count)
        k = k + dig_count
    mod_num = x % 10 ** k
    x //= 10 ** k
    x += mod_num * 10 ** (dig_count - len(str(mod_num)))
    return x


n = int(input())
j = int(input())
print(rotate(n, j))

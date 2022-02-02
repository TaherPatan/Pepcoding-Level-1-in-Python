def inverse_num(num):
    num_inverse = 0
    num = str(abs(num))
    count = 1
    for i in range(len(num) - 1, -1, -1):
        num_inverse += count * 10 ** (int(num[i]) - 1)
        count += 1
    return num_inverse


n = int(input())
print(inverse_num(n))
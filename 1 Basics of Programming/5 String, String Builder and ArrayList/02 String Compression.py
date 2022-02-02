n = input()
temp = ''
temp1 = ''
i = 0
while i < len(n):
    count = 1
    while i < len(n) - 1 and n[i] == n[i + 1]:
        i += 1
        count += 1
    temp += n[i]
    if count > 1:
        temp1 += n[i] + str(count)
    else:
        temp1 += n[i]
    i += 1
print(temp)
print(temp1)

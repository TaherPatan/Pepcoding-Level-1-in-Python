n = int(input())
m = int(input())
a1 = [[int(input()) for j in range(m)] for i in range(n)]
r, c, direction = 0, 0, 0
while True:
    direction = (direction + a1[r][c]) % 4
    if direction == 0:
        c += 1
        if c == m:
            c -= 1
            break
    elif direction == 1:
        r += 1
        if r == n:
            r -= 1
            break
    elif direction == 2:
        c -= 1
        if c == -1:
            c += 1
            break
    elif direction == 3:
        r -= 1
        if r == -1:
            r += 1
            break
print(r)
print(c)

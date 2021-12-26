n = int(input())
sp = n * 2 - 3
st = 1
for rows in range(1, n + 1):
    for star in range(1, st + 1):
        print(f'{star}\t', end='')
    for spaces in range(1, sp + 1):
        print('\t', end='')
    if rows == n:
        st -= 1
    for star in range(st, 0, -1):
        print(f'{star}\t', end='')
    print()
    st += 1
    sp -= 2

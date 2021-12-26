n = input()
for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):
        a = n[i:j]
        b = a[::-1]
        if a == b:
            print(n[i:j])

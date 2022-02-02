t = int(input())
for i in range(t):
    num = int(input())
    flag = True
    for j in range(2, int(num**0.5)+1):
        if num % j == 0:
            flag = False
            break
    if flag:
        print('prime')
    else:
        print('not prime')

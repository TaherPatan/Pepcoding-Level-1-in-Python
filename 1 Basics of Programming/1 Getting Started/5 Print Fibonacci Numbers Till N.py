def fibonacci(num):
    a, b = 0, 1
    if num == 0:
        print(num)
    elif num == 1:
        print(num)
    else:
        print(0)
        print(1)
        for i in range(2, num):
            c, a = a + b, b
            b = c
            print(c)


fibonacci_index = int(input())
fibonacci(fibonacci_index)

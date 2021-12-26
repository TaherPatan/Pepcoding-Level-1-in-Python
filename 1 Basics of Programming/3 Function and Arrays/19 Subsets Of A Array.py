n = int(input())
a1 = [int(input()) for i in range(n)]
for i in range(0, (1 << n)):
    dec = i
    printer_str = ''
    for j in range(1, n + 1):
        rem = dec % 2
        dec = dec // 2
        if rem != 0:
            printer_str = str(a1[-j]) + '\t' + printer_str
        else:
            printer_str = '-\t' + printer_str
    print(printer_str)

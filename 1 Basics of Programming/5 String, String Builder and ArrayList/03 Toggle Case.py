def togglecase(st):
    lst = list(st)
    for i in range(len(lst)):
        if lst[i].isupper():
            lst[i] = lst[i].lower()
        elif lst[i].lower():
            lst[i] = lst[i].upper()
    lst = ''.join(lst)
    print(lst)


if __name__ == '__main__':
    st = input()
    togglecase(st)
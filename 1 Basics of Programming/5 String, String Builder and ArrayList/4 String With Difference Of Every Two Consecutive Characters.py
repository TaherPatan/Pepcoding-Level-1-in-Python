def printstring(st):
    st = list(st)
    for i in range(len(st) - 1, 0, -1):
        st.insert(i, str(ord(st[i]) - ord(st[i - 1])))
    st = ''.join(st)
    return st


if __name__ == '__main__':
    st = input()
    print(printstring(st))

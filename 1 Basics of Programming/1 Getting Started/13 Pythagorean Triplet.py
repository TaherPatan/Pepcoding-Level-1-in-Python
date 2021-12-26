import sys


def pythagorean_triplet(b):
    if b[0] ** 2 + b[1] ** 2 == b[2] ** 2:
        return 'true'
    elif b[0] ** 2 + b[2] ** 2 == b[1] ** 2:
        return 'true'
    elif b[1] ** 2 + b[2] ** 2 == b[0] ** 2:
        return 'true'
    else:
        return 'false'


a = [int(x) for x in sys.stdin.read().split()]
print(pythagorean_triplet(a))

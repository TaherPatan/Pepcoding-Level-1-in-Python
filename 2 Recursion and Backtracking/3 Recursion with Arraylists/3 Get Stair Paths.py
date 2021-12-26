def get_stair_paths(n):
    if n == 0:
        return ['']
    elif n < 0:
        return []
    pathsfromnm1 = get_stair_paths(n - 1)
    pathsfromnm2 = get_stair_paths(n - 2)
    pathsfromnm3 = get_stair_paths(n - 3)
    pathsfromn = []
    for i in pathsfromnm1:
        pathsfromn.append(('1' + i))
    for i in pathsfromnm2:
        pathsfromn.append(('2' + i))
    for i in pathsfromnm3:
        pathsfromn.append(('3' + i))
    return pathsfromn


if __name__ == '__main__':
    n = int(input())
    ans = get_stair_paths(n)
    print("[" + ', '.join(ans) + "]")

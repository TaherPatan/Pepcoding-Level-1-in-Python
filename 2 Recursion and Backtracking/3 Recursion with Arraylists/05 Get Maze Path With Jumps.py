import sys
sys.setrecursionlimit(10000)


def get_maze_path(sr, sc, dr, dc):
    final_path = []
    if sr > dr or sc > dc:
        return []
    elif sr == dr and sc == dc:
        return ['']
    for jump in range(1, dc - sc + 1):
        path1 = get_maze_path(sr, sc + jump, dr, dc)
        final_path += ['h' + str(jump) + j for j in path1]
    for jump in range(1, dr - sr + 1):
        path2 = get_maze_path(sr + jump, sc, dr, dc)
        final_path += ['v' + str(jump) + j for j in path2]
    for jump in range(1, max(dr - sr + 1, dc - sc + 1)):
        if jump > dr - sr or jump > dc - sc:
            break
        path2 = get_maze_path(sr + jump, sc + jump, dr, dc)
        final_path += ['d' + str(jump) + j for j in path2]
    return final_path


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    ans = get_maze_path(0, 0, n - 1, m - 1)
    print("[" + ', '.join(ans) + "]")

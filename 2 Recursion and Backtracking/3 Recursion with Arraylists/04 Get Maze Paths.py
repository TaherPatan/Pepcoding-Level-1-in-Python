def get_maze_path(sr, sc, dr, dc):
    if sr > dr or sc > dc:
        return []
    elif sr == dr and sc == dc:
        return ['']
    path1 = get_maze_path(sr, sc + 1, dr, dc)
    path2 = get_maze_path(sr + 1, sc, dr, dc)
    final_path = ['h' + i for i in path1]
    final_path += ['v' + i for i in path2]
    return final_path


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    ans = get_maze_path(0, 0, n - 1, m - 1)
    print("[" + ', '.join(ans) + "]")

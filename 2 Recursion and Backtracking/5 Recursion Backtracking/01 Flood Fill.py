def flood_fill(maze, sr, sc, asf, visited):
    if sr < 0 or sr >= len(maze) or sc < 0 or sc >= len(maze[0]) or maze[sr][sc] == 1 or visited[sr][sc]:
        return
    if sr == len(maze) - 1 and sc == len(maze[0]) - 1:
        print(asf)
        return
    visited[sr][sc] = True
    flood_fill(maze, sr - 1, sc, asf + 't', visited)
    flood_fill(maze, sr, sc - 1, asf + 'l', visited)
    flood_fill(maze, sr + 1, sc, asf + 'd', visited)
    flood_fill(maze, sr, sc + 1, asf + 'r', visited)
    visited[sr][sc] = False


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited_arr = [[False] * m for _ in range(n)]
    flood_fill(arr, 0, 0, "", visited_arr)

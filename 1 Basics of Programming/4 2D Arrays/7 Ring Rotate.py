def get_one_d_array(lst, shell, rows, cols):
    row_min = shell - 1
    col_min = shell - 1
    row_max = rows - shell
    col_max = cols - shell
    spiral_array = []
    for k in range(row_min, row_max + 1):
        spiral_array.append(lst[k][col_min])
    col_min += 1
    for k in range(col_min, col_max + 1):
        spiral_array.append(lst[row_max][k])
    row_max -= 1
    for k in range(row_max, row_min - 1, -1):
        spiral_array.append(lst[k][col_max])
    col_max -= 1
    for k in range(col_max, col_min - 1, -1):
        spiral_array.append(lst[row_min][k])
    row_min += 1
    return spiral_array


def fill_two_d_shell_from_one_d(lst, spiral_arr, shell, rows, cols):
    count = 0
    row_min = shell - 1
    col_min = shell - 1
    row_max = rows - shell
    col_max = cols - shell
    for k in range(row_min, row_max + 1):
        lst[k][shell - 1] = spiral_arr[count]
        count += 1
    col_min += 1
    for k in range(col_min, col_max + 1):
        lst[rows - shell][k] = spiral_arr[count]
        count += 1
    row_max -= 1
    for k in range(row_max, row_min - 1, -1):
        lst[k][cols - shell] = spiral_arr[count]
        count += 1
    col_max -= 1
    for k in range(col_max, col_min - 1, -1):
        lst[shell - 1][k] = spiral_arr[count]
        count += 1
    row_min += 1


n = int(input())
m = int(input())
arr1 = [[int(input()) for _ in range(m)] for _ in range(n)]
shell_no = int(input())
rotations = int(input())
spiral = get_one_d_array(arr1, shell_no, n, m)
rotations = rotations % len(spiral)
front = spiral[0:-rotations:1]
back = spiral[-rotations::1]
spiral = back + front
fill_two_d_shell_from_one_d(arr1, spiral, shell_no, n, m)
for row in arr1:
    for col in row:
        print(col, end=' ')
    print()

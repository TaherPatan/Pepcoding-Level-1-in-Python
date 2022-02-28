class Node:
    def __init__(self, data):
        self.data, self.left, self.right = data, None, None


def construct_binary_tree(arr):
    root = Node(int(arr.pop(0)))
    stack = [[root, 0]]
    for element in arr:
        if element != 'n':
            new_node = Node(int(element))
            if stack[-1][1] == 0:
                stack[-1][0].left = new_node
                stack[-1][1] += 1
            elif stack[-1][1] == 1:
                stack[-1][0].right = new_node
                stack.pop()
            stack.append([new_node, 0])
        else:
            stack[-1][1] += 1
            if stack[-1][1] > 1:
                stack.pop()
    return root


def display_binary_tree(start_node):
    if not start_node:
        return
    print(f'{start_node.left.data if start_node.left else "."} <- {start_node.data} -> '
          f'{start_node.right.data if start_node.right else "."}')
    display_binary_tree(start_node.left)
    display_binary_tree(start_node.right)


def target_sum_pair(start_node):
    if not start_node:
        return []
    return target_sum_pair(start_node.left) + [start_node.data] + target_sum_pair(start_node.right)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    val = int(input())
    arr = target_sum_pair(root)
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] < val:
            i += 1
        elif val < arr[i] + arr[j]:
            j -= 1
        else:
            print(f'{arr[i]} {arr[j]}')
            i += 1
            j -= 1

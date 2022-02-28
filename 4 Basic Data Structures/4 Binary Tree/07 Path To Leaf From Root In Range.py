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
    print(f'{start_node.left.data if start_node.left else "."} <-- {start_node.data} --> '
          f'{start_node.right.data if start_node.right else "."}')
    display_binary_tree(start_node.left)
    display_binary_tree(start_node.right)


def root_to_leaf_path(start_node, path, start_val, end_val):
    if not start_node:
        return
    if not start_node.left and not start_node.right:
        path = f'{path}{start_node.data} '
        if start_val <= sum(list(map(int, path.split()))) <= end_val:
            print(path)
        return
    path = f'{path}{start_node.data} '
    root_to_leaf_path(start_node.left, path, start_val, end_val)
    root_to_leaf_path(start_node.right, path, start_val, end_val)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    range_start, range_end = int(input()), int(input())
    root_to_leaf_path(root, '', range_start, range_end)

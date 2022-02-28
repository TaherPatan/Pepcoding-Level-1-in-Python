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


def largest_bst_tree_root(start_node):
    global biggest_size, biggest_size_data
    if not start_node:
        return float('-inf'), float('inf'), 0
    max_left, min_left, size_left = largest_bst_tree_root(start_node.left)
    max_right, min_right, size_right = largest_bst_tree_root(start_node.right)
    if max_left < start_node.data < min_right:
        if biggest_size < size_left + size_right + 1:
            biggest_size, biggest_size_data = size_left + size_right + 1, start_node.data
        return max(start_node.data, max(max_left, max_right)), min(start_node.data, min(min_left, min_right)), size_left + size_right + 1
    return max(start_node.data, max(max_left, max_right)), min(start_node.data, min(min_left, min_right)), 0


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    biggest_size, biggest_size_data = 0, 0
    largest_bst_tree_root(root)
    print(f'{biggest_size_data}@{biggest_size}')

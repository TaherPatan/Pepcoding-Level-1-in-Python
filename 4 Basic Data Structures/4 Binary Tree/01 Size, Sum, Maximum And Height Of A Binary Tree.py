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


def binary_tree_size(start_node):
    if not start_node:
        return 0
    return binary_tree_size(start_node.left) + binary_tree_size(start_node.right) + 1


def binary_tree_sum(start_node):
    if not start_node:
        return 0
    return binary_tree_sum(start_node.left) + binary_tree_sum(start_node.right) + start_node.data


def binary_tree_max(start_node):
    if not start_node:
        return float('-inf')
    return max(start_node.data, max(binary_tree_max(start_node.left), binary_tree_max(start_node.right)))


def binary_tree_height(start_node):
    if not start_node:
        return -1
    return max(binary_tree_height(start_node.left), binary_tree_height(start_node.right)) + 1


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    print(binary_tree_size(root))
    print(binary_tree_sum(root))
    print(binary_tree_max(root))
    print(binary_tree_height(root))

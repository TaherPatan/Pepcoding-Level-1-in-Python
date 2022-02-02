class Node:
    def __init__(self, data):
        self.data, self.children = data, []


def construct_generic_tree(arr):
    root = Node(arr.pop(0))
    stack = [root]
    for element in arr:
        if element == -1:
            stack.pop()
            continue
        child = Node(element)
        stack[-1].children.append(child)
        stack.append(child)
    return root


def display_generic_tree(start_node):
    print(f'{start_node.data} -> ', end='')
    for child in start_node.children:
        print(child.data, end=', ')
    print('.')
    for child in start_node.children:
        display_generic_tree(child)


def ceil_floor(start_node, val):
    global ceil, floor
    if floor < start_node.data < val:
        floor = start_node.data
    if val < start_node.data < ceil:
        ceil = start_node.data
    for child in start_node.children:
        ceil_floor(child, val)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    ceil, floor = 2147483647, -2147483648
    ceil_floor(root, int(input()))
    print(f'CEIL = {ceil}')
    print(f'FLOOR = {floor}')

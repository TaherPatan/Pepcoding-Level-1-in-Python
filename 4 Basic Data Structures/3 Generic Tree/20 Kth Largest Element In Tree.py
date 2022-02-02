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


def kth_largest(start_node, val):
    global floor
    if floor < start_node.data < val:
        floor = start_node.data
    for child in start_node.children:
        kth_largest(child, val)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    floor, temp_val = float('-inf'), float('inf')
    for _ in range(int(input())):
        kth_largest(root, temp_val)
        floor, temp_val = float('-inf'), floor
    print(temp_val)

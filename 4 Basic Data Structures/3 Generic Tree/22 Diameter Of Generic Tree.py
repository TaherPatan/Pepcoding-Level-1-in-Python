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


def height(start_node):
    global diameter
    max_height, second_max_height = -1, -1
    for child in start_node.children:
        child_height = height(child)
        if max_height < child_height:
            max_height, second_max_height = child_height, max_height
        elif second_max_height < child_height:
            second_max_height = child_height
    diameter = max(diameter, max_height + second_max_height + 2)
    return max_height + 1


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    diameter = float('-inf')
    height(root)
    print(f'{diameter}')

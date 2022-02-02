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


def get_tail(tail):
    while tail.children:
        tail = tail.children[0]
    return tail


def find_in_tree(start_node, find_val):
    if start_node.data == find_val:
        return 'true'
    for child in start_node.children:
        flag = find_in_tree(child, find_val)
        if flag == 'true':
            return 'true'
    return 'false'


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    print(find_in_tree(root, int(input())))
    print()

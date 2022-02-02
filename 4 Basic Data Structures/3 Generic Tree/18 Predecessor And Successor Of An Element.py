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


def predecessor_successor(start_node, val):
    global predecessor, successor, state
    if not state:
        if start_node.data != val:
            predecessor = start_node.data
        else:
            state = 1
    elif state == 1:
        successor = start_node.data
        state = 2
    for child in start_node.children:
        predecessor_successor(child, val)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    predecessor, successor, state = None, None, 0
    predecessor_successor(root, int(input()))
    print(f'Predecessor = {predecessor}' if predecessor else f'Predecessor = Not found')
    print(f'Successor = {successor}' if successor else f'Successor = Not found')

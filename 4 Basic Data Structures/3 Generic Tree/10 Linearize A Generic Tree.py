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


def linearize_tree(start_node):
    if not start_node.children:
        return start_node
    tail = linearize_tree(start_node.children[0])
    for i in range(1, len(start_node.children)):
        tail.children.append(start_node.children[i])
        tail = linearize_tree(start_node.children[i])
    start_node.children = [start_node.children[0]]
    return tail


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    linearize_tree(root)
    display_generic_tree(root)
    print()

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


def remove_leaves(start_node):
    remover_index = []
    for i in range(len(start_node.children)):
        if start_node.children[i].children:
            remove_leaves(start_node.children[i])
        else:
            remover_index.append(i)
    for i in reversed(remover_index):
        start_node.children.pop(i)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    remove_leaves(root)
    display_generic_tree(root)

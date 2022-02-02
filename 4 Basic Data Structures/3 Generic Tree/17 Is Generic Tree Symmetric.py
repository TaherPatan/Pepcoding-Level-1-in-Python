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


def symmetric_trees(node1, node2):
    if len(node1.children) != len(node2.children):
        return False
    for (child1, child2) in zip(node1.children, reversed(node1.children)):
        if not symmetric_trees(child1, child2):
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root1 = construct_generic_tree(lst)
    print(str(symmetric_trees(root1, root1)).lower())

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


def display_generic_tree_size(start_node):
    global size
    size += 1
    for child in start_node.children:
        display_generic_tree_size(child)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    size = 0
    root = construct_generic_tree(lst)
    display_generic_tree_size(root)
    print(size)

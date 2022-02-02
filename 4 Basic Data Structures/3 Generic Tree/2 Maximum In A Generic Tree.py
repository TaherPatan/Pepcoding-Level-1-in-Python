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


def display_generic_tree_max(start_node):
    global max_val
    max_val = max(start_node.data, max_val)
    for child in start_node.children:
        display_generic_tree_max(child)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    max_val = root.data
    display_generic_tree_max(root)
    print(max_val)

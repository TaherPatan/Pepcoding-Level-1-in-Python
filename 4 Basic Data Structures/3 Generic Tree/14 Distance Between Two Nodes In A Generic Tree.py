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


def node_to_root_path(start_node, find_val):
    if start_node.data == find_val:
        return [start_node.data]
    for child in start_node.children:
        if path := node_to_root_path(child, find_val):
            path.append(start_node.data)
            return path
    return []


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    full_path1 = node_to_root_path(root, int(input()))
    full_path2 = node_to_root_path(root, int(input()))
    while full_path1 and full_path2 and full_path1[-1] == full_path2[-1]:
        full_path1.pop()
        full_path2.pop()
    print(len(full_path1) + len(full_path2))

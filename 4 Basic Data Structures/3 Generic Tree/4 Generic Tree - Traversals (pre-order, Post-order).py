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


def tree_traversal(start_node):
    print(f'Node Pre {start_node.data}')
    for child in start_node.children:
        print(f'Edge Pre {start_node.data}--{child.data}')
        tree_traversal(child)
        print(f'Edge Post {start_node.data}--{child.data}')
    print(f'Node Post {start_node.data}')


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    tree_traversal(root)

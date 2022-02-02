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


def level_order_traversal(start_node):
    queue = [start_node]
    while queue:
        for child in queue[0].children:
            queue.append(child)
        print(queue.pop(0).data, end=' ')
    print('.')


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    level_order_traversal(root)

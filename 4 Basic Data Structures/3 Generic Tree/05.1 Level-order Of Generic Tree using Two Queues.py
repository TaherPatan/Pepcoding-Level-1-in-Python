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
    queue1 = [start_node]
    queue2 = []
    while queue1 or queue2:
        for element in queue1:
            print(element.data, end=' ')
            queue2.extend(element.children)
        queue1 = queue2
        queue2 = []
    print('.')


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    level_order_traversal(root)

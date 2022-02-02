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
    stack1 = [start_node]
    stack2 = []
    while stack1 or stack2:
        while stack1:
            print(stack1[-1].data, end=' ')
            for child in stack1.pop().children:
                stack2.append(child)
        print()
        while stack2:
            print(stack2[-1].data, end=' ')
            for child in reversed(stack2.pop().children):
                stack1.append(child)
        print()


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    level_order_traversal(root)

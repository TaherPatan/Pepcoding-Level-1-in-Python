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


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    stack = [[root, 0]]
    pre, post = [root.data], []
    while stack:
        if stack[-1][1] < len(stack[-1][0].children):
            pre.append(stack[-1][0].children[stack[-1][1]].data)
            stack[-1][1] += 1
            stack.append([stack[-1][0].children[stack[-1][1] - 1], 0])
        else:
            post.append(stack.pop()[0].data)
    for ele in pre:
        print(ele, end=' ')
    print()
    for ele in post:
        print(ele, end=' ')

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


def find_max_subtree(start_node):
    global max_sum, max_sum_node
    curr_sum = start_node.data
    for child in start_node.children:
        curr_sum += find_max_subtree(child)
    if max_sum < curr_sum:
        max_sum_node = start_node
        max_sum = curr_sum
    return curr_sum


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    root = construct_generic_tree(lst)
    max_sum, max_sum_node = float('-inf'), None
    find_max_subtree(root)
    print(f'{max_sum_node.data}@{max_sum}')

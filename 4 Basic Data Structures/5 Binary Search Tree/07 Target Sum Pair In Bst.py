class Node:
    def __init__(self, data):
        self.data, self.left, self.right = data, None, None


def construct_binary_tree(arr):
    root = Node(int(arr.pop(0)))
    stack = [[root, 0]]
    for element in arr:
        if element != 'n':
            new_node = Node(int(element))
            if stack[-1][1] == 0:
                stack[-1][0].left = new_node
                stack[-1][1] += 1
            elif stack[-1][1] == 1:
                stack[-1][0].right = new_node
                stack.pop()
            stack.append([new_node, 0])
        else:
            stack[-1][1] += 1
            if stack[-1][1] > 1:
                stack.pop()
    return root


def display_binary_tree(start_node):
    if not start_node:
        return
    print(f'{start_node.left.data if start_node.left else "."} <- {start_node.data} -> '
          f'{start_node.right.data if start_node.right else "."}')
    display_binary_tree(start_node.left)
    display_binary_tree(start_node.right)


def find_in_bst(start_node, val):
    if not start_node:
        return False
    if start_node.data == val:
        return True
    if start_node.data < val:
        return find_in_bst(start_node.right, val)
    elif val < start_node.data:
        return find_in_bst(start_node.left, val)


def target_sum_pair(root_node, start_node, val):
    if not start_node:
        return
    target_sum_pair(root_node, start_node.left, val)
    if start_node.data < (complement := val - start_node.data):
        if find_in_bst(root_node, complement):
            print(f'{start_node.data} {complement}')
    target_sum_pair(root_node, start_node.right, val)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    target_sum_pair(root, root, int(input()))

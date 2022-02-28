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


def bst_max(start_node):
    if not start_node:
        return float('-inf')
    return max(start_node.data, bst_max(start_node.right))


def remove_node_bst(start_node, val):
    if start_node.data == val:
        if not (start_node.left or start_node.right):
            return None
        elif not start_node.left and start_node.right:
            return start_node.right
        elif not start_node.right and start_node.left:
            return start_node.left
        else:
            start_node.data = bst_max(start_node.left)
            remove_node_bst(start_node.left, start_node.data)
            return start_node
    if val < start_node.data:
        start_node.left = remove_node_bst(start_node.left, val)
    elif start_node.data < val:
        start_node.right = remove_node_bst(start_node.right, val)
    return start_node


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    root = remove_node_bst(root, int(input()))
    display_binary_tree(root)

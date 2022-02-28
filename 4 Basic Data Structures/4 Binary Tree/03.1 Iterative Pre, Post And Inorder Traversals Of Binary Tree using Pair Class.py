class Node:
    def __init__(self, data):
        self.data, self.left, self.right = data, None, None


class Pair:
    def __init__(self, node):
        self.node = node
        self.state = 0


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
    print(f'{start_node.left.data if start_node.left else "."} <-- {start_node.data} --> '
          f'{start_node.right.data if start_node.right else "."}')
    display_binary_tree(start_node.left)
    display_binary_tree(start_node.right)


def binary_tree_traversals(start_node):
    stack = [Pair(start_node)]
    preorder, inorder, postorder = f'', f'', f''
    while stack:
        if not stack[-1].state:
            preorder = f'{preorder}{stack[-1].node.data} '
            stack[-1].state += 1
            if stack[-1].node.left:
                stack.append(Pair(stack[-1].node.left))
        elif stack[-1].state == 1:
            inorder = f'{inorder}{stack[-1].node.data} '
            stack[-1].state += 1
            if stack[-1].node.right:
                stack.append(Pair(stack[-1].node.right))
        else:
            postorder = f'{postorder}{stack[-1].node.data} '
            stack.pop()
    print(preorder)
    print(inorder)
    print(postorder)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    binary_tree_traversals(root)

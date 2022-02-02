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
    print(f'{start_node.left.data if start_node.left else "."} <-- {start_node.data} --> '
          f'{start_node.right.data if start_node.right else "."}')
    display_binary_tree(start_node.left)
    display_binary_tree(start_node.right)


def binary_tree_traversals(start_node):
    stack = [[start_node, 0]]
    preorder, inorder, postorder = f'', f'', f''
    while stack:
        if not stack[-1][1]:
            preorder = f'{preorder}{stack[-1][0].data} '
            stack[-1][1] += 1
            if stack[-1][0].left:
                stack.append([stack[-1][0].left, 0])
        elif stack[-1][1] == 1:
            inorder = f'{inorder}{stack[-1][0].data} '
            stack[-1][1] += 1
            if stack[-1][0].right:
                stack.append([stack[-1][0].right, 0])
        else:
            postorder = f'{postorder}{stack[-1][0].data} '
            stack.pop()
    print(preorder)
    print(inorder)
    print(postorder)


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    binary_tree_traversals(root)

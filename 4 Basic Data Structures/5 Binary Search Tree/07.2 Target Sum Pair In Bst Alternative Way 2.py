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
    print(f'{start_node.left.data if start_node.left else "."} <- {start_node.data} -> '
          f'{start_node.right.data if start_node.right else "."}')
    display_binary_tree(start_node.left)
    display_binary_tree(start_node.right)


def target_sum_pair(start_node, target):
    left_stack, right_stack = [Pair(start_node)], [Pair(start_node)]
    left, right = normal_inorder_tree_traversal(left_stack), reverse_inorder_tree_traversal(right_stack)
    while left.data < right.data:
        if left.data + right.data < target:
            left = normal_inorder_tree_traversal(left_stack)
        elif target < left.data + right.data:
            right = reverse_inorder_tree_traversal(right_stack)
        else:
            print(f'{left.data} {right.data}')
            left = normal_inorder_tree_traversal(left_stack)
            right = reverse_inorder_tree_traversal(right_stack)


def normal_inorder_tree_traversal(left_stack):
    while left_stack:
        if not left_stack[-1].state:
            left_stack[-1].state += 1
            if left_stack[-1].node.left:
                left_stack.append(Pair(left_stack[-1].node.left))
        elif left_stack[-1].state == 1:
            left_stack[-1].state += 1
            if left_stack[-1].node.right:
                left_stack.append(Pair(left_stack[-1].node.right))
                return left_stack[-2].node
            return left_stack[-1].node
        else:
            left_stack.pop()


def reverse_inorder_tree_traversal(right_stack):
    while right_stack:
        if not right_stack[-1].state:
            right_stack[-1].state += 1
            if right_stack[-1].node.right:
                right_stack.append(Pair(right_stack[-1].node.right))
        elif right_stack[-1].state == 1:
            right_stack[-1].state += 1
            if right_stack[-1].node.left:
                right_stack.append(Pair(right_stack[-1].node.left))
                return right_stack[-2].node
            return right_stack[-1].node
        else:
            right_stack.pop()


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    val = int(input())
    target_sum_pair(root, val)

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


def print_k_levels_down(start_node, counter, blocker_node):
    if not start_node or start_node == blocker_node:
        return
    if not counter:
        print(start_node.data)
        return
    print_k_levels_down(start_node.left, counter - 1, blocker_node)
    print_k_levels_down(start_node.right, counter - 1, blocker_node)


def find_given_node(start_node, val):
    if not start_node:
        return []
    if start_node.data == val:
        return [start_node]
    found = find_given_node(start_node.left, val)
    if found:
        found.append(start_node)
        return found
    found = find_given_node(start_node.right, val)
    if found:
        found.append(start_node)
        return found
    return []


if __name__ == '__main__':
    n = int(input())
    lst = list(map(str, input().split()))
    root = construct_binary_tree(lst)
    found_val, k = int(input()), int(input())
    target_node = find_given_node(root, found_val)
    print_k_levels_down(target_node[0], k, None)
    k -= 1
    i = 1
    while k > -1 and i < len(target_node):
        print_k_levels_down(target_node[i], k, target_node[i - 1])
        k -= 1
        i += 1

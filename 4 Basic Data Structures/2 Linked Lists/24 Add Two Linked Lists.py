class Node:
    def __init__(self, data):
        self.data, self.next = data, None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def add_first(self, data):
        if self.head is None and self.tail is None and self.size == 0:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_at(self, index, data):
        if index < 0 or self.size < index:
            print('Invalid arguments')
            return
        elif index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return
        temp = self.get_node_at(index - 1)
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        if index == self.size:
            self.tail = new_node
        self.size += 1

    def add_last(self, data):
        if self.head is None and self.tail is None and self.size == 0:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def get_node_at(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def display_ll(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


def add_linked_lists(node1, node2, p1, p2, result):
    if p1 == p2 == 0:
        return 0
    if p1 < p2:
        carry = add_linked_lists(node1, node2.next, p1, p2 - 1, result)
        data = node2.data + carry
    elif p2 < p1:
        carry = add_linked_lists(node1.next, node2, p1 - 1, p2, result)
        data = node1.data + carry
    elif p1 == p2:
        carry = add_linked_lists(node1.next, node2.next, p1 - 1, p2 - 1, result)
        data = node1.data + node2.data + carry
    carry = data // 10
    result.add_first(data % 10)
    return carry


if __name__ == '__main__':
    try:
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()
        n = int(input())
        lst = list(map(int, input().split()))
        for element in lst:
            linked_list_1.add_last(element)
        n = int(input())
        lst = list(map(int, input().split()))
        for element in lst:
            linked_list_2.add_last(element)
        linked_list_1.display_ll()
        linked_list_2.display_ll()
        result = LinkedList()
        carry = add_linked_lists(linked_list_1.head, linked_list_2.head, linked_list_1.size, linked_list_2.size, result)
        if carry:
            result.add_first(carry)
        result.display_ll()
        result.add_first(int(input()))
        result.add_last(int(input()))
        result.display_ll()
    except EOFError as e:
        pass

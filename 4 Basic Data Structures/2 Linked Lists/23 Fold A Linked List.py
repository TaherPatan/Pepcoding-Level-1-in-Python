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

    def fold_ll(self, right, counter):
        if not right:
            return
        self.fold_ll(right.next, counter + 1)
        if self.size // 2 <= counter:
            global left
            if self.size // 2 == counter:
                left.next, right.next = right, None
                self.tail = right
                return
            left.next, right.next = right, left.next
            left = left.next.next


if __name__ == '__main__':
    try:
        linked_list = LinkedList()
        n = int(input())
        lst = list(map(int, input().split()))
        for element in lst:
            linked_list.add_last(element)
        left = linked_list.head
        linked_list.display_ll()
        linked_list.fold_ll(linked_list.head, 0)
        linked_list.display_ll()
        command = input()
        linked_list.add_first(int(command))
        command = input()
        linked_list.add_last(int(command))
        linked_list.display_ll()
    except EOFError as e:
        pass

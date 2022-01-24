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

    def remove_first(self):
        if self.head is None:
            print('List is empty')
            return
        elif self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return
        self.head = self.head.next
        self.size -= 1

    def remove_at(self, index):
        if self.size == 0:
            print('List is empty')
            return
        elif index < 0 or self.size <= index:
            print('Invalid arguments')
            return
        elif self.size == 1 and index == 0:
            self.head = self.size = None
            self.size -= 1
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        elif index == self.size - 1:
            temp = self.get_node_at(self.size - 2)
            temp.next = None
            self.tail = temp
            self.size -= 1
            return
        temp = self.get_node_at(index - 1)
        temp.next = temp.next.next
        self.size -= 1

    def remove_last(self):
        if self.head is None:
            print('List is empty')
            return
        elif self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return
        temp = self.get_node_at(self.size - 2)
        temp.next = None
        self.tail = temp
        self.size -= 1

    def get_first(self):
        if self.size == 0:
            return 'List is empty'
        return self.head.data

    def get_at(self, index):
        if self.size == 0:
            return 'List is empty'
        elif index < 0 or self.size <= index:
            return 'Invalid arguments'
        temp = self.get_node_at(index)
        return temp.data

    def get_node_at(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def get_last(self):
        if self.size == 0:
            return 'List is empty'
        return self.tail.data

    def display_ll(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def k_reversed(self, k):
        if self.size < k:
            return
        sz = self.size
        k_reversed_linked_list = LinkedList()
        for _ in range(k):
            k_reversed_linked_list.add_first(self.get_first())
            self.remove_first()
        i = 0
        reversed_ll = LinkedList()
        while k <= self.size:
            if i % k == 0 and i != 0:
                k_reversed_linked_list.tail.next = reversed_ll.head
                k_reversed_linked_list.tail = reversed_ll.tail
                reversed_ll = LinkedList()
                i = 0
            else:
                reversed_ll.add_first(self.get_first())
                self.remove_first()
                i += 1
        if reversed_ll.size:
            k_reversed_linked_list.tail.next = reversed_ll.head
            k_reversed_linked_list.tail = reversed_ll.tail
        if self.size:
            k_reversed_linked_list.tail.next = self.head
            k_reversed_linked_list.tail = self.tail
        self.head = k_reversed_linked_list.head
        self.tail = k_reversed_linked_list.tail
        self.size = sz


if __name__ == '__main__':
    try:
        linked_list = LinkedList()
        n = int(input())
        lst = list(map(int, input().split()))
        for element in lst:
            linked_list.add_last(element)
        linked_list.display_ll()
        linked_list.k_reversed(int(input()))
        linked_list.display_ll()
        command = input()
        linked_list.add_first(int(command))
        command = input()
        linked_list.add_last(int(command))
        linked_list.display_ll()
    except EOFError as e:
        pass

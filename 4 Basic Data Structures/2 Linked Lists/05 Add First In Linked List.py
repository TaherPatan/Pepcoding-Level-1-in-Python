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
            self.size = 0
            return
        self.head = self.head.next
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
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.data

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


if __name__ == '__main__':
    linked_list = LinkedList()
    while (command := input()) != 'quit':
        if command[0:8] == 'addFirst':
            linked_list.add_first(int(command[9:]))
        elif command[0:7] == 'addLast':
            linked_list.add_last(int(command[8:]))
        elif command[0:8] == 'getFirst':
            print(linked_list.get_first())
        elif command[0:5] == 'getAt':
            print(linked_list.get_at(int(command[6:])))
        elif command[0:7] == 'getLast':
            print(linked_list.get_last())
        elif command[0:11] == 'removeFirst':
            linked_list.remove_first()
        elif command[0:4] == 'size':
            print(linked_list.size)
        elif command[0:7] == 'display':
            linked_list.display_ll()

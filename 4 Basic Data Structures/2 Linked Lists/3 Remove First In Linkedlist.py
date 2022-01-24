class Node:
    def __init__(self, data):
        self.data, self.next = data, None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

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

    def display_ll(self):
        if not self.size:
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


if __name__ == '__main__':
    linked_list = LinkedList()
    while (command := input()) != 'quit':
        if command[0:7] == 'addLast':
            linked_list.add_last(int(command[8:]))
        elif command[0:11] == 'removeFirst':
            linked_list.remove_first()
        elif command[0:4] == 'size':
            print(linked_list.size)
        elif command[0:7] == 'display':
            linked_list.display_ll()

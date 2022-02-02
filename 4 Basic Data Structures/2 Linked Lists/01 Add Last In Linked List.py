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

    def display_ll(self):
        if not self.size:
            return
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linked_list = LinkedList()
    while (command := input()) != 'quit':
        linked_list.add_last(int(command[8:]))
    linked_list.display_ll()
    print(linked_list.size)
    if linked_list.size:
        print(linked_list.tail.data)

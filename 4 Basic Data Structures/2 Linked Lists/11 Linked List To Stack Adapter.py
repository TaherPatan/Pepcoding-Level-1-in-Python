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
        if not self.size:
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def reverse_ll_di(self):
        if self.size == 0:
            return 'List is empty'
        elif self.size == 1:
            return
        temp_head = self.head
        temp_back_index = self.size - 1
        for i in range(self.size // 2):
            temp_back = self.get_node_at(temp_back_index)
            temp_head.data, temp_back.data = temp_back.data, temp_head.data
            temp_back_index -= 1
            temp_head = temp_head.next

    def reverse_ll_pi(self):
        if self.size == 0:
            return 'List is empty'
        elif self.size == 1:
            return
        temp = self.tail
        temp_back_index = self.size - 2
        for i in range(self.size - 1):
            temp_replacer = self.get_node_at(temp_back_index)
            temp.next = temp_replacer
            temp = temp_replacer
            temp_back_index -= 1
        self.head, self.tail = self.tail, self.head
        self.tail.next = None


class LLStack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):
        self.stack.add_last(data)

    def pop(self):
        if self.stack.size == 0:
            return 'Stack underflow'
        element = self.stack.tail.data
        self.stack.remove_last()
        return element

    def top(self):
        if self.stack.size == 0:
            return 'Stack underflow'
        return self.stack.tail.data

    def size(self):
        return self.stack.size


if __name__ == '__main__':
    try:
        linked_list_stack = LLStack()
        while (command := input()) != 'quit':
            if command[0:4] == 'push':
                linked_list_stack.push(int(command[5:]))
            elif command[0:3] == 'pop':
                print(linked_list_stack.pop())
            elif command[0:3] == 'top':
                print(linked_list_stack.top())
            elif command[0:4] == 'size':
                print(linked_list_stack.size())
    except EOFError as e:
        pass

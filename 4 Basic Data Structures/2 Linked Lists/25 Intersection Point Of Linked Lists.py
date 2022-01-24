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


def find_intersection(l1, l2):
    if l1.size < l2.size:
        diff = l2.size - l1.size
        temp1 = l2.get_node_at(diff)
        temp2 = l1.head
    else:
        diff = l1.size - l2.size
        temp1 = l1.get_node_at(diff)
        temp2 = l2.head
    while temp1 != temp2:
        temp1 = temp1.next
        temp2 = temp2.next
    print(temp1.data)


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
        li = int(input())
        di = int(input())
        if li == 1:
            n = linked_list_1.get_node_at(di)
            if linked_list_2.size > 0:
                linked_list_2.tail.next = n
            else:
                linked_list_2.head = n
            linked_list_2.tail = linked_list_1.tail
            linked_list_2.size += linked_list_1.size - di
        else:
            n = linked_list_2.get_node_at(di)
            if linked_list_1.size > 0:
                linked_list_1.tail.next = n
            else:
                linked_list_1.head = n
            linked_list_1.tail = linked_list_2.tail
            linked_list_1.size += linked_list_2.size - di
        find_intersection(linked_list_1, linked_list_2)
    except EOFError as e:
        pass

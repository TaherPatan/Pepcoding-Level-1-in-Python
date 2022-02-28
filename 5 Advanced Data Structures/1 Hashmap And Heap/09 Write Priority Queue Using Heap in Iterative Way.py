class PriorityQueue:
    def __init__(self):
        self.pq = []

    def add(self, data):
        if not self.pq:
            self.pq.append(data)
            return
        self.pq.append(data)
        self.up_heapify()

    def remove(self):
        if not self.pq:
            return 'Underflow'
        self.pq[0], self.pq[len(self.pq) - 1] = self.pq[len(self.pq) - 1], self.pq[0]
        return_element = self.pq.pop()
        self.down_heapify()
        return return_element

    def peek(self):
        return 'Underflow' if not self.pq else self.pq[0]

    def size(self):
        return len(self.pq)

    def up_heapify(self):
        child_index = len(self.pq) - 1
        parent_index = (child_index - 1) // 2
        while 0 <= parent_index and self.pq[child_index] < self.pq[parent_index]:
            self.pq[parent_index], self.pq[child_index] = self.pq[child_index], self.pq[parent_index]
            parent_index, child_index = (parent_index - 1) // 2, parent_index

    def down_heapify(self):
        if 2 < len(self.pq):
            if self.pq[1] < self.pq[2]:
                child_index = 1
            else:
                child_index = 2
        else:
            child_index = 1
        parent_index = 0
        while child_index < len(self.pq) and self.pq[child_index] < self.pq[parent_index]:
            self.pq[parent_index], self.pq[child_index] = self.pq[child_index], self.pq[parent_index]
            parent_index = child_index
            if child_index * 2 + 1 < len(self.pq) and child_index * 2 + 2 < len(self.pq):
                if self.pq[child_index * 2 + 1] < self.pq[child_index * 2 + 2]:
                    child_index = child_index * 2 + 1
                else:
                    child_index = child_index * 2 + 2
            elif child_index * 2 + 1 < len(self.pq):
                child_index = child_index * 2 + 1
            else:
                child_index = len(self.pq) + 1


if __name__ == '__main__':
    pq = PriorityQueue()
    while (command := input()) != 'quit':
        if 'add' in command:
            pq.add(int(command[4:]))
        elif 'remove' in command:
            print(pq.remove())
        elif 'peek' in command:
            print(pq.peek())
        elif 'size' in command:
            print(pq.size())

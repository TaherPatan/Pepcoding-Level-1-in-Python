class PriorityQueue:
    def __init__(self, arr):
        self.pq = arr.copy()
        for i in range((len(self.pq) - 2) // 2, -1, -1):
            self.down_heapify(i)

    def add(self, data):
        self.pq.append(data)
        self.up_heapify(len(self.pq) - 1)

    def remove(self):
        if not self.pq:
            return 'Underflow'
        self.pq[0], self.pq[len(self.pq) - 1] = self.pq[len(self.pq) - 1], self.pq[0]
        return_element = self.pq.pop()
        self.down_heapify(0)
        return return_element

    def peek(self):
        return 'Underflow' if not self.pq else self.pq[0]

    def size(self):
        return len(self.pq)

    def up_heapify(self, child_index):
        if not child_index:
            return
        parent_index = (child_index - 1) // 2
        if self.pq[child_index] < self.pq[parent_index]:
            self.pq[child_index], self.pq[parent_index] = self.pq[parent_index], self.pq[child_index]
            self.up_heapify(parent_index)

    def down_heapify(self, parent_index):
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        minimum_index = parent_index
        if left_child_index < len(self.pq) and self.pq[left_child_index] < self.pq[minimum_index]:
            minimum_index = left_child_index
        if right_child_index < len(self.pq) and self.pq[right_child_index] < self.pq[minimum_index]:
            minimum_index = right_child_index
        if minimum_index != parent_index:
            self.pq[minimum_index], self.pq[parent_index] = self.pq[parent_index], self.pq[minimum_index]
            self.down_heapify(minimum_index)


if __name__ == '__main__':
    pq = PriorityQueue([12, 8, -40, 11, 16, 9, 3, 119, -786, 754, 19, 1])
    while pq.pq:
        print(pq.remove())

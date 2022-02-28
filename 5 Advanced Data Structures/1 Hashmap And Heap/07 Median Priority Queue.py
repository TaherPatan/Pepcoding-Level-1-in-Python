import heapq


class MedianPriorityQueue:
    def __init__(self):
        self.max_pq, self.min_pq = [], []
        heapq.heapify(self.max_pq)
        heapq.heapify(self.min_pq)

    def add(self, element):
        if self.min_pq and self.min_pq[0] < element:
            heapq.heappush(self.min_pq, element)
        else:
            heapq.heappush(self.max_pq, -element)
        self.median_pq_size_adjuster()

    def peek(self):
        if not self.size():
            return 'Underflow'
        elif len(self.min_pq) <= len(self.max_pq):
            return -self.max_pq[0]
        else:
            return self.min_pq[0]

    def remove(self):
        if not self.size():
            return 'Underflow'
        elif len(self.min_pq) <= len(self.max_pq):
            return_element = -heapq.heappop(self.max_pq)
        else:
            return_element = heapq.heappop(self.min_pq)
        self.median_pq_size_adjuster()
        return return_element

    def size(self):
        return len(self.min_pq) + len(self.max_pq)

    def median_pq_size_adjuster(self):
        if len(self.max_pq) < len(self.min_pq) - 1:
            heapq.heappush(self.max_pq, -heapq.heappop(self.min_pq))
        elif len(self.min_pq) < len(self.max_pq) - 1:
            heapq.heappush(self.min_pq, -heapq.heappop(self.max_pq))


if __name__ == '__main__':
    median_pq = MedianPriorityQueue()
    while (command := input()) != 'quit':
        if 'add' in command:
            median_pq.add(int(command[4:]))
        elif 'remove' in command:
            print(median_pq.remove())
        elif 'peek' in command:
            print(median_pq.peek())
        elif 'size' in command:
            print(median_pq.size())

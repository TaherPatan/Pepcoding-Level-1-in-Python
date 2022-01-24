class Queue:
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.front = 0
        self.filled_size = 0
        self.queue = [0] * self.queue_size

    def size(self):
        return self.filled_size

    def add(self, data):
        if self.filled_size < self.queue_size:
            self.queue[(self.front + self.filled_size) % self.queue_size] = data
            self.filled_size += 1
        else:
            print('Queue overflow')

    def peek(self):
        if self.filled_size:
            return self.queue[self.front]
        else:
            return 'Queue underflow'

    def remove(self):
        if self.filled_size > 0:
            self.front = (self.front + 1) % self.queue_size
            self.filled_size -= 1
            return self.queue[self.front - 1]
        else:
            return 'Queue underflow'

    def display(self):
        for i in range(self.filled_size):
            print(self.queue[(self.front + i) % self.queue_size], end=' ')
        print()


if __name__ == '__main__':
    normal_queue = Queue(int(input()))
    while (command := input()) != 'quit':
        if 'add' in command:
            normal_queue.add(int(command[4:]))
        elif 'remove' in command:
            print(normal_queue.remove())
        elif 'peek' in command:
            print(normal_queue.peek())
        elif 'size' in command:
            print(normal_queue.size())
        elif 'display' in command:
            normal_queue.display()

class Queue:
    def __init__(self):
        self.main_stack = []
        self.helper_stack = []

    def size(self):
        return len(self.main_stack)

    def add(self, data):
        self.main_stack.append(data)

    def peek(self):
        if self.main_stack:
            self.helper_stack = [self.main_stack.pop() for _ in range(len(self.main_stack) - 1)]
            element = self.main_stack.pop()
            self.helper_stack.append(element)
            self.main_stack = [self.helper_stack.pop() for _ in range(len(self.helper_stack))]
            self.helper_stack = []
            return element
        else:
            return 'Queue underflow'

    def remove(self):
        if self.main_stack:
            self.helper_stack = [self.main_stack.pop() for _ in range(len(self.main_stack) - 1)]
            element = self.main_stack.pop()
            self.main_stack = [self.helper_stack.pop() for _ in range(len(self.helper_stack))]
            self.helper_stack = []
            return element
        else:
            return 'Queue underflow'


if __name__ == '__main__':
    try:
        dynamic_queue = Queue()
        while (command := input()) != 'quit':
            if 'add' in command:
                dynamic_queue.add(int(command[4:]))
            elif 'remove' in command:
                print(dynamic_queue.remove())
            elif 'peek' in command:
                print(dynamic_queue.peek())
            elif 'size' in command:
                print(dynamic_queue.size())
    except EOFError as e:
        pass

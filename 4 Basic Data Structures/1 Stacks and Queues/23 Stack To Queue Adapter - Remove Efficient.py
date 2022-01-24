class Queue:
    def __init__(self):
        self.main_stack = []
        self.helper_stack = []

    def size(self):
        return len(self.main_stack)

    def add(self, data):
        self.helper_stack.append(data)
        self.helper_stack.extend(element for element in self.main_stack)
        self.helper_stack, self.main_stack = [], self.helper_stack

    def peek(self):
        return self.main_stack[-1] if self.main_stack else 'Queue underflow'

    def remove(self):
        return self.main_stack.pop() if self.main_stack else 'Queue underflow'


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

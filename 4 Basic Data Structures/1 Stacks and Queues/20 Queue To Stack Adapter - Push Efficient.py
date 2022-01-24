import queue


class Stack:
    def __init__(self):
        self.mainQ = queue.Queue()
        self.helperQ = queue.Queue()

    def size(self):
        return self.mainQ.qsize()

    def push(self, data):
        self.mainQ.put(data)

    def top(self):
        if self.mainQ.empty():
            return 'Stack underflow'
        for _ in range(self.mainQ.qsize() - 1):
            self.helperQ.put(self.mainQ.get())
        element = self.mainQ.get()
        self.helperQ.put(element)
        self.mainQ = self.helperQ
        return element

    def pop(self):
        if self.mainQ.empty():
            return 'Stack underflow'
        for _ in range(self.mainQ.qsize() - 1):
            self.helperQ.put(self.mainQ.get())
        element = self.mainQ.get()
        self.mainQ = self.helperQ
        return element


if __name__ == '__main__':
    try:
        dynamic_stack = Stack()
        while (command := input()) != 'quit':
            if 'push' in command:
                dynamic_stack.push(int(command[5:]))
            elif 'pop' in command:
                print(dynamic_stack.pop())
            elif 'top' in command:
                print(dynamic_stack.top())
            elif 'size' in command:
                print(dynamic_stack.size())
    except EOFError as e:
        pass

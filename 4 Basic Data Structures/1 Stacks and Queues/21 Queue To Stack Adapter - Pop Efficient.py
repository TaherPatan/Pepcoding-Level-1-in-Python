import queue


class Stack:
    def __init__(self):
        self.mainQ = queue.Queue()
        self.helperQ = queue.Queue()

    def size(self):
        return self.mainQ.qsize()

    def push(self, data):
        if self.mainQ.qsize() == 0:
            self.mainQ.put(data)
            return
        self.helperQ.put(data)
        while self.mainQ.qsize() != 0:
            self.helperQ.put(self.mainQ.get())
        self.mainQ, self.helperQ = self.helperQ, self.mainQ

    def top(self):
        if self.mainQ.empty():
            return 'Stack underflow'
        element = self.mainQ.get()
        self.helperQ.put(element)
        while self.mainQ.qsize() > 0:
            self.helperQ.put(self.mainQ.get())
        self.mainQ, self.helperQ = self.helperQ, self.mainQ
        return element

    def pop(self):
        if self.mainQ.empty():
            return 'Stack underflow'
        return self.mainQ.get()


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

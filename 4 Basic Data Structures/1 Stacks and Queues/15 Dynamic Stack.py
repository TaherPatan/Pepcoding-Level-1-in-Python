class Stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.pointer = -1
        self.stack = [0] * self.stack_size

    def push(self, element):
        if self.stack_size - 1 <= self.pointer:
            self.stack = self.stack + ([0] * self.stack_size)
            self.stack_size = self.stack_size * 2
        self.pointer += 1
        self.stack[self.pointer] = element

    def pop(self):
        if self.pointer > -1:
            self.pointer -= 1
            return self.stack[self.pointer + 1]
        else:
            return 'Stack underflow'

    def top(self):
        if self.pointer > -1:
            return self.stack[self.pointer]
        else:
            return 'Stack underflow'

    def size(self):
        return self.pointer + 1

    def display(self):
        for i in range(self.pointer, -1, -1):
            print(self.stack[i], end=' ')
        print()


if __name__ == '__main__':
    dynamic_stack = Stack(int(input()))
    while (command := input()) != 'quit':
        if 'push' in command:
            dynamic_stack.push(int(command[5:]))
        elif 'pop' in command:
            print(dynamic_stack.pop())
        elif 'top' in command:
            print(dynamic_stack.top())
        elif 'size' in command:
            print(dynamic_stack.size())
        elif 'display' in command:
            dynamic_stack.display()

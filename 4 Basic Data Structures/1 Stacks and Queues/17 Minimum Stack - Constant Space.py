class Stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.pointer = -1
        self.stack = [0] * self.stack_size
        self.min_var = False

    def push(self, element):
        if self.stack_size - 1 <= self.pointer:
            self.stack = self.stack + ([0] * self.stack_size)
            self.stack_size = self.stack_size * 2
        self.pointer += 1
        self.stack[self.pointer] = element if not self.min_var or self.min_var < element else (2 * element) - self.min_var
        self.min_var = element if not self.min_var or element < self.min_var else self.min_var

    def pop(self):
        if self.pointer > -1:
            if self.stack[self.pointer] < self.min_var:
                self.stack[self.pointer], self.min_var = self.min_var, (2 * self.min_var) - self.stack[self.pointer]
            self.pointer -= 1
            return self.stack[self.pointer + 1]
        else:
            return 'Stack underflow'

    def top(self):
        if self.pointer > -1:
            return self.min_var if self.stack[self.pointer] < self.min_var else self.stack[self.pointer]
        else:
            return 'Stack underflow'

    def size(self):
        return self.pointer + 1

    def min(self):
        return self.min_var if -1 < self.pointer else 'Stack underflow'


if __name__ == '__main__':
    try:
        dynamic_stack = Stack(1)
        while (command := input()) != 'quit':
            if 'push' in command:
                dynamic_stack.push(int(command[5:]))
            elif 'pop' in command:
                print(dynamic_stack.pop())
            elif 'top' in command:
                print(dynamic_stack.top())
            elif 'size' in command:
                print(dynamic_stack.size())
            elif 'min' in command:
                print(dynamic_stack.min())
    except EOFError as e:
        pass

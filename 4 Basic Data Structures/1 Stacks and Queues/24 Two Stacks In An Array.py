class TwoStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.pointer1 = -1
        self.pointer2 = self.stack_size
        self.stack = [0] * self.stack_size

    def push1(self, element):
        if self.pointer1 < self.pointer2 - 1:
            self.pointer1 += 1
            self.stack[self.pointer1] = element
        else:
            print('Stack overflow')

    def pop1(self):
        if self.pointer1 > -1:
            self.pointer1 -= 1
            return self.stack[self.pointer1 + 1]
        else:
            return 'Stack underflow'

    def top1(self):
        if self.pointer1 > -1:
            return self.stack[self.pointer1]
        else:
            return 'Stack underflow'

    def size1(self):
        return self.pointer1 + 1

    def push2(self, element):
        if self.pointer1 + 1 < self.pointer2:
            self.pointer2 -= 1
            self.stack[self.pointer2] = element
        else:
            print('Stack overflow')

    def pop2(self):
        if self.pointer2 < self.stack_size:
            self.pointer2 += 1
            return self.stack[self.pointer2 - 1]
        else:
            return 'Stack underflow'

    def top2(self):
        if self.pointer2 < self.stack_size:
            return self.stack[self.pointer2]
        else:
            return 'Stack underflow'

    def size2(self):
        return self.stack_size - self.pointer2


if __name__ == '__main__':
    try:
        dynamic_stack = TwoStack(int(input()))
        while (command := input()) != 'quit':
            if 'push' in command:
                if 'push1' in command:
                    dynamic_stack.push1(int(command[6:]))
                else:
                    dynamic_stack.push2(int(command[6:]))
            elif 'pop' in command:
                if 'pop1' in command:
                    print(dynamic_stack.pop1())
                else:
                    print(dynamic_stack.pop2())
            elif 'top' in command:
                if 'top1' in command:
                    print(dynamic_stack.top1())
                else:
                    print(dynamic_stack.top2())
            elif 'size' in command:
                if 'size1' in command:
                    print(dynamic_stack.size1())
                else:
                    print(dynamic_stack.size2())
    except EOFError as e:
        pass

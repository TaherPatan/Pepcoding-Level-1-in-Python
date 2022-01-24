def solve(op2, op1, optr):
    if optr == '+':
        return op1 + op2
    elif optr == '-':
        return op1 - op2
    elif optr == '*':
        return op1 * op2
    elif optr == '/':
        return op1 // op2


def precedence(optr):
    if optr in '+-':
        return 1
    elif optr in '*/':
        return 2
    else:
        return 0


def infix(exp):
    operators_stack, variables_stack = [], []
    for ch in exp:
        if '0' <= ch <= '9':
            variables_stack.append(int(ch))
        elif ch == '(':
            operators_stack.append(ch)
        elif ch in '+-*/':
            while operators_stack and precedence(ch) <= precedence(operators_stack[-1]):
                variables_stack.append(solve(variables_stack.pop(), variables_stack.pop(), operators_stack.pop()))
            operators_stack.append(ch)
        elif ch == ')':
            while operators_stack[-1] != '(':
                variables_stack.append(solve(variables_stack.pop(), variables_stack.pop(), operators_stack.pop()))
            operators_stack.pop()
    while operators_stack:
        variables_stack.append(solve(variables_stack.pop(), variables_stack.pop(), operators_stack.pop()))
    return variables_stack.pop()


if __name__ == '__main__':
    exp = input()
    exp = exp.replace(" ", "")
    print(infix(exp))

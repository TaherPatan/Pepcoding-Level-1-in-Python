def solve(operators, variables_prefix, variables_postfix):
    op_2_prefix, op_1_prefix = variables_prefix.pop(), variables_prefix.pop()
    op_2_postfix, op_1_postfix = variables_postfix.pop(), variables_postfix.pop()
    op = operators.pop()
    variables_prefix.append(f'{op}{op_1_prefix}{op_2_prefix}')
    variables_postfix.append(f'{op_1_postfix}{op_2_postfix}{op}')


def precedence(optr):
    if optr in '+-':
        return 1
    elif optr in '*/':
        return 2
    else:
        return 0


def prefix(exp):
    operators_stack, variables_prefix_stack, variables_postfix_stack = [], [], []
    for ch in exp:
        if 'a' <= ch <= 'z':
            variables_prefix_stack.append(ch)
            variables_postfix_stack.append(ch)
        elif ch == '(':
            operators_stack.append(ch)
        elif ch in '+-*/':
            while operators_stack and precedence(ch) <= precedence(operators_stack[-1]):
                solve(operators_stack, variables_prefix_stack, variables_postfix_stack)
            operators_stack.append(ch)
        elif ch == ')':
            while operators_stack[-1] != '(':
                solve(operators_stack, variables_prefix_stack, variables_postfix_stack)
            operators_stack.pop()
    while operators_stack:
        solve(operators_stack, variables_prefix_stack, variables_postfix_stack)
    return variables_prefix_stack.pop(), variables_postfix_stack.pop()


if __name__ == '__main__':
    exp = input()
    pre, post = prefix(exp)
    print(post)
    print(pre)

def solve_equation(op2, op1, optr):
    if optr == '+':
        return op1 + op2
    elif optr == '-':
        return op1 - op2
    elif optr == '*':
        return op1 * op2
    elif optr == '/':
        return op1 / op2


def solve_operations(infix_variables_stack, prefix_variables_stack, result_stack, op):
    op_2_infix, op_1_infix = infix_variables_stack.pop(), infix_variables_stack.pop()
    op_2_prefix, op_1_prefix = prefix_variables_stack.pop(), prefix_variables_stack.pop()
    op_2_result, op_1_result = result_stack.pop(), result_stack.pop()
    infix_variables_stack.append(f'({op_1_infix}{op}{op_2_infix})')
    prefix_variables_stack.append(f'{op}{op_1_prefix}{op_2_prefix}')
    result_stack.append(int(solve_equation(op_2_result, op_1_result, op)))


def postfix_evaluation(exp):
    infix_variables_stack, prefix_variables_stack, result_stack = [], [], []
    for ch in exp:
        if '0' <= ch <= '9':
            infix_variables_stack.append(ch)
            prefix_variables_stack.append(ch)
            result_stack.append(int(ch))
        else:
            solve_operations(infix_variables_stack, prefix_variables_stack, result_stack, ch)
    return infix_variables_stack.pop(), prefix_variables_stack.pop(), result_stack.pop()


if __name__ == '__main__':
    exp = input()
    infix, pre, res = postfix_evaluation(exp)
    print(res)
    print(infix)
    print(pre)

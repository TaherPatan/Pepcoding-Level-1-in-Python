def solve_equation(op1, op2, optr):
    if optr == '+':
        return op1 + op2
    elif optr == '-':
        return op1 - op2
    elif optr == '*':
        return op1 * op2
    elif optr == '/':
        return op1 / op2


def solve_operations(infix_variables_stack, postfix_variables_stack, result_stack, op):
    op_1_infix, op_2_infix = infix_variables_stack.pop(), infix_variables_stack.pop()
    op_1_prefix, op_2_prefix = postfix_variables_stack.pop(), postfix_variables_stack.pop()
    op_1_result, op_2_result = result_stack.pop(), result_stack.pop()
    infix_variables_stack.append(f'({op_1_infix}{op}{op_2_infix})')
    postfix_variables_stack.append(f'{op_1_prefix}{op_2_prefix}{op}')
    result_stack.append(int(solve_equation(op_1_result, op_2_result, op)))


def prefix_evaluation(exp):
    infix_variables_stack, postfix_variables_stack, result_stack = [], [], []
    for ch in reversed(exp):
        if '0' <= ch <= '9':
            infix_variables_stack.append(ch)
            postfix_variables_stack.append(ch)
            result_stack.append(int(ch))
        else:
            solve_operations(infix_variables_stack, postfix_variables_stack, result_stack, ch)
    return infix_variables_stack.pop(), postfix_variables_stack.pop(), result_stack.pop()


if __name__ == '__main__':
    exp = input()
    infix, post, res = prefix_evaluation(exp)
    print(res)
    print(infix)
    print(post)

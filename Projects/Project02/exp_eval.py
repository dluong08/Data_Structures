from array_stack import (ArrayStack, empty_stack, push, pop, peek, is_empty, size)


def postfix_eval(input_string: str) -> float:
    """Evaluates the given RPN expression.

    Args:
        input_string: an RPN expression

    Returns:
        The result of the expression evaluation

    Raises:
        ValueError: if the input is not well-formed
        ZeroDivisionError: if the input would cause division by zero
    """
    if len(input_string) == 0:
        raise ValueError("Empty Input")
    stack = empty_stack()
    output_string = input_string.split()
    for i in output_string:
        try:
            push(stack, float(i))
        except ValueError:
            if stack.size < 2:
                raise ValueError("Insufficient Opperads")
            op_1 = pop(stack)
            op_2 = pop(stack)
            if i in ['+', '-', '/', '//', '*', '**']:
                push(stack, do_operation(op_1, op_2, i))
            else:
                raise ValueError("Invalid Token")
    if stack.size > 1:
        raise ValueError("Too Many Operands")
    return pop(stack)


def infix_to_postfix(input_string: str) -> str:
    """Converts the given infix string to RPN.

    Args:
        input_string: an infix expression

    Returns:
        The equivalent expression in RPN
    """
    stack = empty_stack()
    output_string = input_string.split()
    string = ''
    for i in output_string:
        try:
            string += str(int(i)) + " "
        except ValueError:
            if i == ")":
                while peek(stack) != "(":
                    item = pop(stack)
                    string += item + " "
                pop(stack)
            if not is_empty(stack):
                if i == '*' or i == '/' or i == '//':
                    while not is_empty(
                        stack) and peek(stack) != '+' and peek(
                            stack) != '-' and peek(stack) != '(':
                        string += pop(stack) + ' '
            if i == '+' or i == '-':
                while not is_empty(stack) and peek(stack) != '(':
                    string += pop(stack) + ' '
            if i != ')':
                push(stack, i)
    while stack.size > 1:
        item = pop(stack)
        string += item + ' '
    string += pop(stack)
    return string


def do_operation(op_1, op_2, operator):
    if operator == '+':
        return float(op_2) + float(op_1)
    elif operator == '-':
        return float(op_2) - float(op_1)
    elif operator == '*':
        return float(op_2) * float(op_1)
    elif operator == '/':
        try:
            return float(op_2) / float(op_1)
        except ZeroDivisionError:
            raise ZeroDivisionError
    elif operator == '//':
        try:
            return float(op_2) // float(op_1)
        except ZeroDivisionError:
            raise ZeroDivisionError
    elif operator == '**':
        return float(op_2) ** float(op_1)

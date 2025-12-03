from collections import deque


def evaluate_rpn(expression: str) -> int:
    stack = deque()
    for char in expression.split():
        if char == '+':
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a + b)
        elif char == '-':
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(b - a)
        elif char == '/':
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(b / a)
        elif char == '*':
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a * b)
        else:
            stack.append(char)

    return stack.pop()



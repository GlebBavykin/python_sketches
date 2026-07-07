from collections import deque


def evaluate_pn(expression: str, reverse=True) -> int:
    """
    Evaluate polish expressions and return result
    """
    stack: deque = deque()
    tokens = expression.split()
    if not reverse:
        tokens = tokens[::-1]

    for char in tokens:
        if char == "+":
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a + b)
        elif char == "-":
            a, b = int(stack.pop()), int(stack.pop())
            if reverse:
                stack.append(b - a)
            else:
                stack.append(a - b)
        elif char == "/":
            a, b = int(stack.pop()), int(stack.pop())
            if reverse:
                stack.append(b / a)
            else:
                stack.append(a / b)
        elif char == "*":
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a * b)
        else:
            stack.append(char)

    return stack.pop()

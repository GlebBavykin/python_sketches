def validate_parentheses(data: str) -> bool:
    """
    Check if the parentheses has pairs
    """
    stack = []
    match = {
        "[": "]",
        "{": "}",
        "(": ")",
    }
    for char in data:
        if char in ("[", "{", "("):
            stack.append(char)
        elif char in ("]", "}", ")"):
            if len(stack) == 0:
                # граничное условие, когда сначала приходит закрывающая скоба
                return False
            if char == match[stack.pop()]:
                continue
            else:
                # условие, когда предпоследняя скобка не соответствует текущей
                return False
    if len(stack) == 0:
        return True
    else:
        # граничное условие, когда в стеке остались скобки без пары
        return False

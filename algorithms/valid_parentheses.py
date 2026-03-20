def is_valid_parentheses(data: str) -> bool:
    """
    Check if the parentheses has pairs
    """
    stack = []
    parentheses_map = {
        "[": "]",
        "{": "}",
        "(": ")",
    }
    for char in data:
        if char in parentheses_map.keys():
            stack.append(char)
        elif char in parentheses_map.values():
            if not stack or parentheses_map[stack.pop()] != char:
                # если первая приходит закрывающая скобка, или предыдущая скобка непарна текущей
                return False
    return len(stack) == 0

def Valid(s):
    stack = []
    bracket= {')': '(',
              '}': '{',
              ']': '['}

    for char in s:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket.keys():
            if not stack or bracket[char] != stack.pop():
                return False
        else:
            return False

    # print(type(not stack))
    return not stack


inputs = ""
result = Valid(inputs)
print(result)

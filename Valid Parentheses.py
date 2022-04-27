def isValid(self, s: str) -> bool:
    stack = []
    openings = ('(', '{', '[')
    closings = (')', '}', ']')
    d = {'(' : ')', '[': ']', '{': '}'}

    for char in s:
        if char in d:
            stack.append(char)
        else:
            if not stack:
                return False
            if char != d[stack.pop()]:
                return False

    return not len(stack)

print(isValid(0, "()"))



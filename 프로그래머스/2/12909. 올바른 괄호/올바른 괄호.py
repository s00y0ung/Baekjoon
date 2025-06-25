def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append('(')
        else:
            if not stack:
                stack.append(-1)
                break
            stack.pop()

    return len(stack) == 0
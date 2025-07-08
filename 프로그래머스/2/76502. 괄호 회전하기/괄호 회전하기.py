def solution(s):
    answer = 0

    for i in range(len(s)):
        stack = []
        ss = s[i:] + s[:i]

        for c in ss:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            elif not stack:
                stack.append(-1)
                break
            elif c == '}' and stack[-1] == "{":
                stack.pop(-1)
            elif c == ')' and stack[-1] == "(":
                stack.pop(-1)
            elif c == ']' and stack[-1] == "[":
                stack.pop(-1)
        if not stack:
            answer += 1

    return answer
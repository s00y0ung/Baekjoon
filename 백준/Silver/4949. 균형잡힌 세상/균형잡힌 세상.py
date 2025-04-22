import sys
input = sys.stdin.readline


s = input().rstrip()
while s != '.':
    s_list = list(s)
    stack = []
    s_flag = 0
    for i in s_list:
        if i == '(' or i == '[':
            stack.append(i)
        elif i ==')':
            if not stack:
                s_flag = 1
                break
            t = stack.pop(len(stack)-1)
            if t != '(':
                s_flag = 1
                break
        elif i ==']':
            if not stack:
                s_flag = 1
                break
            t = stack.pop(len(stack)-1)
            if t != '[':
                s_flag = 1
                break
    if not stack and s_flag == 0:
        print('yes')
    else:
        print('no')
    s = input().rstrip()

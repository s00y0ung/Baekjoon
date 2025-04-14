import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    i_list = list(map(int, input().split()))
    if i_list[0] == 1:
        stack.append(i_list[1])
    elif i_list[0] == 2:
        if not stack:
            print(-1)
        else:
            print(stack.pop(len(stack)-1))
    elif i_list[0] == 3:
        print(len(stack))
    elif i_list[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    elif i_list[0] == 5:
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])
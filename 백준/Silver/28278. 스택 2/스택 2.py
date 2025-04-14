import sys
input = sys.stdin.readline

N = int(input())

stack = []
output = []

for _ in range(N):
    i_list = list(map(int, input().split()))
    if i_list[0] == 1:
        stack.append(i_list[1])
    elif i_list[0] == 2:
        output.append(-1 if not stack else stack.pop())
    elif i_list[0] == 3:
        output.append(len(stack))
    elif i_list[0] == 4:
        output.append(1 if not stack else 0)
    elif i_list[0] == 5:
        output.append(-1 if not stack else stack[-1])

print('\n'.join(map(str,output)))
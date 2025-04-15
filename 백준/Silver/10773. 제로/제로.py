import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    k = int(input())
    if k == 0:
        if len(stack) != 0:
            stack.pop()
    else:
        stack.append(k)
print(sum(stack))
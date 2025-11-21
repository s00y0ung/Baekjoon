import sys
input = sys.stdin.readline

N = int(input())
stack = []
ans = []
p = 0
for i in range(1,N+1):
    n = int(input())

    while p < n and p < N:
        p += 1
        stack.append(p)
        ans.append('+')

    if n == stack[-1]:
        stack.pop()
        ans.append('-')
    else:
        ans.append('NO')
        break
        
if ans[-1] == 'NO':
    print("NO")
else:
    print('\n'.join(ans))
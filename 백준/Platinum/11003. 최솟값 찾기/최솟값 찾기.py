import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
d = list(map(int, input().split()))

que = deque()
ans = []
for c in range(N):
    while que and que[-1][1] > d[c]:
        que.pop()
    que.append([c,d[c]])
    if que[-1][0] - que[0][0] >= L:
        que.popleft()
    ans.append(que[0][1])
print(*ans)
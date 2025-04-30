from collections import deque

N = int(input())
d_list = list(map(int, input().split()))
idx_list = deque([i for i in range(1, N+1)])
d = deque(d_list)

p = 0
ans = []
for _ in range(N):
    ans.append(idx_list[0])
    p = d.popleft()
    idx_list.popleft()
    if p > 0:
        p -= 1
    d.rotate(p*-1)#시계방향 회전은 양수, 반시계는 음수
    idx_list.rotate(p*-1)
print(*ans)
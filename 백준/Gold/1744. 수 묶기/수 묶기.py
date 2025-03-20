import sys
import heapq
input = sys.stdin.readline

N = int(input())

heapP = []
heapM = []
ans = []

for i in range(N):
    t = int(input())
    if t <= 0:
        heapM.append(t)
    elif t == 1:
        ans.append(1)
    else:
        heapP.append(-1*t)

heapq.heapify(heapP)
heapq.heapify(heapM)

# positive
while len(heapP) > 1:
    h1 = heapq.heappop(heapP)
    h2 = heapq.heappop(heapP)
    ans.append(h1*h2)
if len(heapP) == 1:
    ans.append(heapP[0] * -1)

# negative
while len(heapM) > 1:
    h1 = heapq.heappop(heapM)
    h2 = heapq.heappop(heapM)
    ans.append(h1*h2)
if len(heapM) == 1:
    ans.append(heapM[0])

print(sum(ans))
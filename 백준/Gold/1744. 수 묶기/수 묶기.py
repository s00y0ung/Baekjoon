import sys
input = sys.stdin.readline

N = int(input())

heapP = []
heapM = []
ans = 0

for i in range(N):
    t = int(input())
    if t <= 0:
        heapM.append(t)
    elif t == 1:
        ans += 1
    else:
        heapP.append(t)

heapP.sort(reverse=True)
heapM.sort()

# positive
for i in range(0, len(heapP),2):
    if i+1 < len(heapP):
        ans += (heapP[i] * heapP[i+1])
    else:
        ans += heapP[i]

# negative
for i in range(0, len(heapM), 2):
    if i+1 < len(heapM):
        ans += (heapM[i]* heapM[i+1])
    else:
        ans += (heapM[i])

print(ans)
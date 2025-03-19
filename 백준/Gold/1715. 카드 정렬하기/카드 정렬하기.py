import sys, heapq
input = sys.stdin.readline

N = int(input())

cardHeap = []
for i in range(N):
    cardHeap.append(int(input()))
heapq.heapify(cardHeap)

cnt = 0
while len(cardHeap) > 1:
    c1 = heapq.heappop(cardHeap)
    c2 = heapq.heappop(cardHeap)

    cnt += c1+c2
    heapq.heappush(cardHeap,c1+c2)

print(cnt)

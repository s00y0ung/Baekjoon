import sys
import heapq
input = sys.stdin.readline

N = int(input())
m_heap = []
p_heap = []
for i in range(N):
    num = int(input())
    if num == 0:
        if not m_heap and not p_heap:
            print(0)
        elif m_heap and not p_heap:
            print(heapq.heappop(m_heap)*-1)
        elif not m_heap and p_heap:
            print(heapq.heappop(p_heap))
        else:
            if m_heap[0] <= p_heap[0]:
                print(heapq.heappop(m_heap)*-1)
            else:
                print(heapq.heappop(p_heap))
    else:
        if num > 0:
            heapq.heappush(p_heap, num)
        else:
            heapq.heappush(m_heap, -1*num)
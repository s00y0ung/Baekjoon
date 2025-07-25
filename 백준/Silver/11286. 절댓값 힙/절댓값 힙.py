#11286,1377
import sys
input = sys.stdin.readline
from queue import PriorityQueue
n = int(input())
que = PriorityQueue()
for i in range(n):
    k = int(input())
    if k == 0:
        if que.qsize() == 0:
            print(0)
            continue
        print(que.get()[1])
    else:
        priority = abs(k)*2
        if k < 0:
            priority -= 1
        que.put((priority,k))
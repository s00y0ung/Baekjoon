from collections import deque
import sys
input = sys.stdin.readline

def check(n, n_list):
    if n == 1:
        dq.appendleft(n_list[1])
    elif n == 2:
        dq.append(n_list[1])
    elif n == 3:
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif n == 4:
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif n == 5:
        print(len(dq))
    elif n == 6:
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif n == 7:
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif n == 8:
        if not dq:
            print(-1)
        else:
            print(dq[len(dq)-1])

N = int(input())
dq = deque()
for _ in range(N):
    n_list = list(map(int, input().split()))
    check(n_list[0], n_list)
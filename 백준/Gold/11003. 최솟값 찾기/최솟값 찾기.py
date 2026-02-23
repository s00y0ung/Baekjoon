import sys
from collections import deque
input = sys.stdin.readline

def main():
    N ,L = map(int, input().split())
    num = list(map(int, input().split()))
    d = deque()
    ans = []
    for i in range(N):
        if d and i-d[0][1] >= L:
            d.popleft()
        while d and d[-1][0] > num[i]:
            d.pop()
        d.append((num[i],i))
        ans.append(d[0][0])
    print(*ans)
    
if __name__ == '__main__':
    main()
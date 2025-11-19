from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, L = map(int, input().split())
    que = deque()
    num = list(map(int, input().split()))
    ans = []
    for i in range(N):
        while que and que[-1][1] > num[i]:
            que.pop()
        que.append([i, num[i]])
        if i - que[0][0] >= L:
            que.popleft()
        ans.append(que[0][1])
        
    print(*ans)

if __name__ == '__main__':
    main()
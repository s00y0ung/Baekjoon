import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    income = [[0,i] for i in range(n+1)]
    g = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int, input().split())
        g[a].append(b)
        income[b][0] += 1

    que = []
    for i in range(1,n+1):
        if income[i][0] == 0:
            que.append(i)
    ans = []
    while que:
        cur = que.pop(0)
        ans.append(cur)
        for i in g[cur]:
            income[i][0] -= 1
            if income[i][0] == 0:
                que.append(i)
    print(*ans)

if __name__ == '__main__':
    main()
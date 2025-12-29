import sys
input = sys.stdin.readline

def main():
    N,M = map(int, input().split())
    income = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        income[b] += 1

    que = []
    for i in range(1, N+1):
        if income[i] == 0:
            que.append(i)

    ans = []
    while que:
        cur = que.pop(0)
        ans.append(cur)
        for i in graph[cur]:
            if income[i] != 0:
                income[i] -= 1
                if income[i] == 0:
                    que.append(i)
    print(*ans)

if __name__ == "__main__":
    main()
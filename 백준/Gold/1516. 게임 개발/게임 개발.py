import sys
input = sys.stdin.readline

def main():
    N = int(input())

    graph = [[] for _ in range(N+1)]
    income = [0]*(N+1)
    time = [0]*(N+1)
    ans = [0]*(N+1)
    que = []

    for i in range(1,1+N):
        tmp = input().split()
        time[i] = int(tmp[0])
        for j in tmp[1:-1]:
            graph[int(j)].append(i)
        income[i] = len(tmp[1:-1])
        if income[i] == 0:
            que.append(i)
            ans[i] = time[i]

    while que:
        cur = que.pop(0)
        for i in graph[cur]:
            income[i] -= 1
            ans[i] = max(ans[i], time[i]+ans[cur])
            if income[i] == 0:
                que.append(i)

    print('\n'.join(list(map(str,ans[1:]))))

if __name__ == "__main__":
    main()
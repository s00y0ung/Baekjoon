import sys
input = sys.stdin.readline

def main():
    n = int(input())
    time = [0 for _ in range(n+1)]
    income = [0 for _ in range(n+1)]
    g = [[] for _ in range(n+1)]
    que = []
    ans = [0] * (n + 1)
    for i in range(n):
        tmp = list(map(int, input().split()))[:-1]
        time[i+1] = tmp[0]
        income[i+1] = len(tmp)-1
        if income[i+1] == 0:
            que.append(i+1)
            ans[i+1] = tmp[0]
        for t in range(1, len(tmp)):
            g[tmp[t]].append(i+1)

    while que:
        cur = que.pop(0)
        for i in g[cur]:
            income[i] -= 1
            ans[i] = max(ans[i], time[i] + ans[cur])
            if income[i] == 0:
                que.append(i)
    print('\n'.join(map(str,ans[1:])))

if __name__ == '__main__':
    main()
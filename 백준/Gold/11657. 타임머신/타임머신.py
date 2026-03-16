import sys
input = sys.stdin.readline

INF = int(1e9)

def bellman_ford(start, g, distance, n, m):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            cur = g[j][0]
            next = g[j][1]
            weight = g[j][2]
            if distance[cur] != INF and distance[next] > distance[cur]+weight:
                distance[next] = distance[cur]+weight
                if i == n-1:
                    return True
    return False

def main():
    n,m = map(int, input().split())
    g = []
    distance = [INF]*(n+1)
    for _ in range(m):
        a,b,c = map(int, input().split())
        g.append((a,b,c))

    if bellman_ford(1,g,distance,n,m):
        print(-1)
    else:
        for d in distance[2:]:
            if d == INF:
                print(-1)
            else:
                print(d)

if __name__ == '__main__':
    main()

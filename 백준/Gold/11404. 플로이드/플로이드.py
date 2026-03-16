import sys
input = sys.stdin.readline
INF = int(1e9)
def main():
    n = int(input())
    m = int(input())
    distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        distance[a][b] = min(c, distance[a][b])
    for i in range(1,n+1):
        distance[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    for dist in distance[1:]:
        print(*[0 if dist[x] == INF else dist[x] for x in range(1,n+1)])

if __name__ == '__main__':
    main()
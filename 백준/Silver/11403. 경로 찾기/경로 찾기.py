import sys
input = sys.stdin.readline

def main():
    n = int(input())
    distance = [[] for _ in range(n)]
    INF = int(1e9)

    for i in range(n):
        distance[i] = list(map(int, input().split()))
        distance[i] = [INF if distance[i][d] == 0 else distance[i][d] for d in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k]+distance[k][j]

    for d in range(n):
        distance[d] = [0 if distance[d][x] == INF else 1 for x in range(n)]
        print(*distance[d])
if __name__ == '__main__':
    main()
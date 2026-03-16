import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    distance = [[1000000 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        distance[a][b] = 1
        distance[b][a] = 1


    for k in range(1,n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k]+distance[k][j]

    k_dist = [0 for _ in range(n+1)]
    for d in range(1,n+1):
        k_dist[d] = sum(distance[d][1:]) - distance[d][d]
    print(k_dist.index(min(k_dist[1:])))

if __name__ == '__main__':
    main()
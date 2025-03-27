def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def dfs(n, ingre, visited):

    for idx in range(len(ingre[n])):
        if ingre[n][idx] != 0 and visited[idx] == 0:
            visited[idx] = visited[n] * ingre[n][idx][1] // ingre[n][idx][0]
            dfs(idx, ingre, visited)


def solve():
    N = int(input())
    ingre = [[0 for j in range(N)] for i in range(N)]
    visited = [0 for i in range(N)]
    lcm = 1

    for i in range(N-1):
        a,b,p,q = map(int, input().split())

        ingre[a][b] = [p,q]
        ingre[b][a] = [q,p]

        lcm *= (p * q)

    visited[0] = lcm
    dfs(0, ingre, visited)
    
    l = visited[0]
    for i in range(len(visited)):
        l = get_gcd(l, visited[i])
    for v in visited:
        print(v//l,end = ' ')
    print()
solve()
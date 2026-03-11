import sys
import math
input = sys.stdin.readline

def bfs(n,d,tmp,g, arr):
    visited = [0]*n
    visited[d] = 1
    que = []
    for q in g[d]:
        que.append(q)

    while que:
        cur = que.pop(0)
        if visited[cur] == 0:
            arr[cur] = arr[cur]*tmp // arr[d]
            visited[cur] = 1
            for k in g[cur]:
                que.append(k)
    arr[d] = tmp
    return arr

def gcd_check(a,b):
    while b > 0:
        a,b = b,a%b
    return a

def main():
    n = int(input())
    arr = [1]*n
    g = [set() for _ in range(n)]

    for _ in range(n-1):
        a,b,p,q = map(int, input().split())
        tmp = arr[a]*arr[b]

        gcd = gcd_check(p,q)
        p,q = p//gcd, q//gcd

        arr = bfs(n,a,tmp*p,g,arr)
        arr = bfs(n,b,tmp*q,g,arr)
        g[a].add(b)
        g[b].add(a)
    gcd = math.gcd(*arr)
    for i in arr:
        print(i//gcd, end = ' ')

if __name__ == '__main__':
    main()
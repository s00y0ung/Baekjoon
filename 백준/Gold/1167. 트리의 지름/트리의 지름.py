import sys
input = sys.stdin.readline

def bfs(tree,v):

    distance = [-1]*len(tree)
    que = [v]
    distance[v] = 0
    while que:
        cur = que.pop()
        for v,e in tree[cur]:
            if distance[v] == -1:
                distance[v] = distance[cur]+e
                que.append(v)
    m = max(distance)
    return distance.index(m), m


def main():
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(1,N+1):
        tmp = list(map(int, input().split()))
        cnt = 1
        while tmp[cnt] != -1:
            tree[tmp[0]].append((tmp[cnt], tmp[cnt+1]))
            cnt = cnt+2

    v,e = bfs(tree,1)
    v,e = bfs(tree,v)
    print(e)


if __name__ == '__main__':
    main()

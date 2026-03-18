import sys
input = sys.stdin.readline

def main():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [-1]*(n+1)
    que = [1]
    while que:
        cur = que.pop(0)
        for i in tree[cur]:
            if visited[i] == -1:
                visited[i] = cur
                que.append(i)
    print('\n'.join(map(str,visited[2:])))

if __name__ == '__main__':
    main()
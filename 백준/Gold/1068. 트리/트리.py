import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    parent = list(map(int, input().split()))
    root = parent.index(-1)
    delete = int(input())

    if root == delete:
        print(0)
        return

    tree = [[] for _ in range(n)]
    for i in range(n):
        if parent[i] != -1 and i != delete:
            tree[parent[i]].append(i)

    que = deque([root])
    visited = [-1]*n
    ans = 0
    while que:
        cur = que.popleft()
        if len(tree[cur]) == 0:
            ans += 1
        for i in tree[cur]:
            if i != delete and visited[i] == -1:
                que.append(i)
                visited[i] = cur
    print(ans)

if __name__ == '__main__':
    main()
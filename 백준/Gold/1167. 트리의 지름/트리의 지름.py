import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, depth):
    global tree, visited

    for v, e in tree[node]:
        if visited[v] == -1:
            visited[v] = depth + e
            dfs(v, depth + e)
    return

if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N+1)]
    visited = [-1 for i in range(N+1)]

    for _ in range(N):
        line = list(map(int, input().split()))
        cnt_node = line[0]

        idx = 1
        while line[idx] != -1 :
            adj_node , adj_cost = line[idx], line[idx+1]
            tree[cnt_node].append((adj_node, adj_cost))
            idx += 2

    visited[1] = 0
    dfs(1,0)
    max_distance = max(visited)
    max_node = visited.index(max_distance)

    visited = [-1 for i in range(N + 1)]
    visited[max_node] = 0
    dfs(max_node , 0)

    print(max(visited))

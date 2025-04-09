import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def unionByRank(rank, a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        rank[b] += 1
        parent[a] = b

V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
rank = [0] * (V+1)
for _ in range(E):
    edges.append(list(map(int, input().split())))
edges.sort(key = lambda x : x[2])

result = 0
count = 0
for e in edges:
    u,v,w = e
    if find(u) == find(v):
        continue
    unionByRank(rank,u,v)
    result += w
    count += 1
    if count >= V-1:
        break
print(result)
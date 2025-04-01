import sys
input = sys.stdin.readline

def union(b,c):
    b_root = find(b)
    c_root = find(c)

    if rank[b_root] > rank[c_root]:
        parent[c_root] = b_root
    elif rank[b_root] < rank[c_root]:
        parent[b_root] = c_root
    else:
        parent[b_root] = c_root
        rank[c_root] += 1

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

for i in range(m):
    a,b,c  = map(int, input().split())
    if a == 0:
        union(b,c)
    elif a == 1:
        b_parent = find(b)
        c_parent = find(c)

        if b_parent == c_parent:
            print("YES")
        else:
            print("NO")
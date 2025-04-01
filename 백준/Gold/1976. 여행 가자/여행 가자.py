def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return

    if parent[x_root] < parent[y_root]:
        parent[x_root] += parent[y_root]
        parent[y_root] = x_root
    else:
        parent[y_root] += parent[x_root]
        parent[x_root] = y_root

def find(x):
    if parent[x] < 0:
        return x
    return find(parent[x])


N = int(input()) # N <= 200
M = int(input()) # M <= 1000

parent = [-1] * (N+1)
graph =[[] for _ in range(N+1)]

for i in range(1, 1+N):
    graph[i] = list(map(int, input().split()))
    graph[i].insert(0,0)
plan = list(map(int, input().split()))

for k in range(1,1+N):
    for i in range(1,len(graph[k])):
        if graph[k][i] == 1:
            union(k, i)

flag = 1
pre = plan[0]
for cur in plan[1:]:
    if find(pre) != find(cur):
        flag = 0
        break
if flag: print("YES")
else: print("NO")
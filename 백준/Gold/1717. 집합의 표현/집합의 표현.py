import sys
input = sys.stdin.readline

# union by rank
#음수일 때 루트 크기 저장, 양수일 땐, 부모 인덱스 저장하는 방식임 ...
def union(b,c):
    b_root = find(b)
    c_root = find(c)

    if b_root == c_root: #이미 같은 집합인 경우
        return

    if parent[b_root] < parent[c_root]: #음수 비교, b의 집합 크기가 더 큰 경우
        parent[b_root] += parent[c_root]
        parent[c_root] = b_root
    else:
        parent[c_root] += parent[b_root]
        parent[b_root] = c_root


def find(x):
    if parent[x] < 0:
        return x
    return find(parent[x])

n, m = map(int, input().split())
parent = [-1 for i in range(n+1)]

for i in range(m):
    a,b,c  = map(int, input().split())
    if a == 0:
        union(b,c)
    elif a == 1:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")
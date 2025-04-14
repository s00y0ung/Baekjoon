import sys
from math import ceil, log
input = sys.stdin.readline

def tree_init(l,r,node):
    if l == r:
        tree[node] = n_list[l]
        return

    mid = (l + r) // 2
    tree_init(l, mid, node*2)
    tree_init(mid+1, r, node*2 + 1)
    tree[node] = min( tree[node*2] , tree[node*2+1])

def get_min(l,r,node, left,right):
    if r < left or right < l:
        return 1000000000
    if left <= l and r <= right:
        return tree[node]
    mid = (l+r) // 2
    m1 = get_min(l, mid, node*2, left, right)
    m2 = get_min(mid+1, r, node*2+1, left, right)
    return min(m1 , m2)

N, M = map(int, input().split())

height = ceil(log(N,2) + 1)
tree = [1000000000] * (2**height)

n_list = []
for _ in range(N):
    n_list.append(int(input()))
tree_init(0, N-1, 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(get_min(0,N-1,1,a-1,b-1))
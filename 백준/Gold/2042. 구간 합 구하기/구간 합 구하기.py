import sys
from math import ceil, log
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

def tree_init(l,r, node):
    if l == r:
        tree[node] = n_list[l]
        return

    mid = (l + r) // 2
    tree_init(l, mid, node * 2)
    tree_init(mid+1, r, node * 2 + 1)
    tree[node] = tree[node*2] + tree[node*2+1]

def tree_update(l, r, node, idx, diff):
    if not (l <= idx <= r):
        return

    tree[node] += diff
    if l == r:
        return

    mid = (l + r) // 2
    tree_update(l, mid, node*2, idx, diff)
    tree_update(mid+1, r, node*2+1, idx, diff)

def interval_sum(l, r, node, left, right):

    if r < left or right < l:
        return 0
    if left <= l and r <= right:
        return tree[node]

    mid = (l + r) // 2
    return interval_sum(l, mid, node*2, left, right) + interval_sum(mid+1, r, node*2+1, left, right)

N, M, K = map(int, input().split())
n_list = []
tree_height = ceil(log(N,2)+1)
tree = [0] * (2**tree_height)

for _ in range(N):
    n_list.append(int(input()))
tree_init(0, N-1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        tree_update(0, N-1, 1, b-1, c-n_list[b-1])
        n_list[b-1] = c
    elif a == 2:
        print(interval_sum(0, N-1, 1, b-1, c-1))
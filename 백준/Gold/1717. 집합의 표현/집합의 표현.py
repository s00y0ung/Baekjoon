import sys
input = sys.stdin.readline

def find(parent,x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(a,b,parent,size):
    root_a = find(parent,a)
    root_b = find(parent,b)

    if root_a == root_b:
        return
    elif size[root_a] > size[root_b]:
        parent[root_b] = root_a
        size[root_a] += size[root_b]
    else:
        parent[root_a] = root_b
        size[root_b] += size[root_a]

def main():
    n,m = map(int, input().split())
    parent = [i for i in range(n+1)]
    size = [1 for _ in range(n+1)]
    for _ in range(m):
        z, a,b = map(int, input().split())
        if z == 0:
            union(a,b,parent,size)
        elif z == 1:
            if find(parent,a) == find(parent,b):
                print('yes')
            else:
                print('no')

if __name__ == '__main__':
    main()
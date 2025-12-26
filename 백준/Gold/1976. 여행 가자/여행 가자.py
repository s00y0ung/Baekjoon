import sys
input = sys.stdin.readline

def find(n,parent):
    while n != parent[n]:
        n = parent[n]
    return n

def union(a,b,size,parent):
    roota = find(a, parent)
    rootb = find(b, parent)

    if roota == rootb: return

    if size[roota] < size[rootb]:
        parent[roota] = rootb
        size[rootb] += size[roota]
    else:
        parent[rootb] = roota
        size[roota] += size[rootb]

def main():
    N = int(input())
    M = int(input())

    parent = [i for i in range(N+1)]
    size = [1]*(N+1)
    for i in range(1,N+1):
        connect = list(map(int, input().split()))
        for j in range(N):
            if connect[j] == 1:
                union(i,j+1,size,parent)

    plan = list(map(int, input().split()))
    plan_root = find(plan[0], parent)
    for p in plan[1:]:
        if plan_root != find(p, parent):
            print('NO')
            return
    print('YES')

if __name__ == "__main__":
    main()
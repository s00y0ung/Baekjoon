import sys
input = sys.stdin.readline

def find(x, parent):
    while x != parent[x]:
        x = parent[x]
    return x

def union(a,b,parent):
    ra = find(a,parent)
    rb = find(b,parent)

    if ra == rb: return
    elif ra > rb:
        parent[rb] = ra
    else:
        parent[ra] = rb


def main():
    n = int(input())
    m = int(input())
    parent = [i for i in range(n+1)]

    for i in range(1,n+1):
        tmp = list(map(int, input().split()))
        for t in range(n):
            if tmp[t] == 1:
                union(i,t+1,parent)

    plan = list(map(int, input().split()))
    rp = find(plan[0], parent)
    for p in plan:
        if rp != find(p,parent):
            print('NO')
            return
    print('YES')

if __name__ == '__main__':
    main()
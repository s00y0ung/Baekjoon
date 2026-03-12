import sys
input = sys.stdin.readline

def main():
    a,b,c = map(int, input().split())
    water = []

    que = [[0,0,c]]
    water.append([0,0,c])
    ans = {c}
    while que:
        cur = que.pop(0)
        for x,y,z in [(0,1,b),(0,2,c),(1,0,a),(1,2,c),(2,0,a),(2,1,b)]:
            if cur[x] != 0:
                tmp = cur[:]
                tmp[x],tmp[y] = max(0,cur[x]+cur[y]-z),min(z,cur[x]+cur[y])
                if tmp not in water:
                    water.append(tmp)
                    que.append(tmp)
                    if tmp[0] == 0:
                        ans.add(tmp[2])
    print(*sorted(ans))

if __name__ == '__main__':
    main()
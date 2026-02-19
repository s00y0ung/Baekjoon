import sys
input = sys.stdin.readline

def main():
    N,M = map(int, input().split())
    a_list = []
    s_list = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        a_list.append(list(map(int, input().split())))
    for x in range(1,N+1):
        for y in range(1, N+1):
            s_list[x][y] = s_list[x-1][y]+s_list[x][y-1]-s_list[x-1][y-1]+a_list[x-1][y-1]
    
    for _ in range(M):
        xs,ys,xe,ye = map(int, input().split())
        print(s_list[xe][ye]-s_list[xe][ys-1]-s_list[xs-1][ye]+s_list[xs-1][ys-1])
main()
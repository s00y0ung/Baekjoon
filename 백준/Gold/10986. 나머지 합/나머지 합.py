import sys
input = sys.stdin.readline

def main():
    N,M = map(int, input().split())
    a_list = list(map(int,input().split()))
    s_list = [0]*(N+1)
    remain = [0]*(M)
    for i in range(1,N+1):
        s_list[i] = s_list[i-1]+a_list[i-1]
        remain[s_list[i]%M] += 1
    ans = remain[0]
    for i in range(M):
        tmp = remain[i]
        ans += max(0, tmp*(tmp+1)//2-tmp)
    print(ans)

main()
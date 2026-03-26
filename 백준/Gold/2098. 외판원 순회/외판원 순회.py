import sys
input = sys.stdin.readline

def search(n,mat,dp,node, chk):
    if chk == (1<<n)-1:
        if mat[node][0] != 0:
            return mat[node][0]
        else:
            return 1e9
    if dp[node][chk] != None:
        return dp[node][chk]

    min_value = 1e9
    for i in range(1, n):
        if (mat[node][i] != 0) and ((chk & (1 << i)) == 0):
            min_value = min(min_value, search(n,mat,dp,i, chk | (1 << i)) + mat[node][i])
    dp[node][chk] = min_value

    return min_value

def main():
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))
    dp = [[None for _ in range(1 << n)] for _ in range(n)]  # 모든 방문 가능 경우의 수

    chk = 1
    print(search(n,mat,dp,0,chk))
if __name__ == '__main__':
    main()

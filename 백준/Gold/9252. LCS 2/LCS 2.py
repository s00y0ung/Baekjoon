import sys
input = sys.stdin.readline

def main():
    s1 = list(input().strip())
    s2 = list(input().strip())

    d = [[[0,''] for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    ans = [0,'']
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1] == s1[j-1]:
                d[i][j][0] = d[i-1][j-1][0]+1
                d[i][j][1] = d[i-1][j-1][1]+s2[i-1]
            else:
                if d[i-1][j][0] > d[i][j-1][0]:
                    d[i][j][0] = d[i-1][j][0]
                    d[i][j][1] = d[i-1][j][1]
                else:
                    d[i][j][0] = d[i][j-1][0]
                    d[i][j][1] = d[i][j-1][1]
            if d[i][j][0] > ans[0]:
                ans = [d[i][j][0], d[i][j][1]]
    print(ans[0])
    if ans[0] != 0:
        print(ans[1])

if __name__ == '__main__':
    main()
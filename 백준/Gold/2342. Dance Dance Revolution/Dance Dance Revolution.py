import sys
input = sys.stdin.readline

def main():
    w = [[-1,2,2,2,2],[2,1,3,4,3],[2,3,1,3,4],[2,4,3,1,3],[2,3,4,3,1]]
    g = list(map(int, input().split()))
    step = [[[1000000 for _ in range(5)] for _ in range(5)] for _ in range(len(g))]
    step[0][0][0] = 0
    s = 1
    for idx in range(len(g)-1):
        n = g[idx]
        for i in range(5):
            if i == n:
                continue
            for j in range(5):
                step[s][i][n] = min(step[s-1][i][j] + w[j][n], step[s][i][n])
        for i in range(5):
            for j in range(5):
                if j == n:
                    continue
                step[s][n][j] = min(step[s-1][i][j] + w[i][n], step[s][n][j])
        s += 1
    minval = 1000000
    for i in range(5):
        for j in range(5):
            minval = min(minval, step[s-1][i][j])

    print(minval)

if __name__ == '__main__':
    main()
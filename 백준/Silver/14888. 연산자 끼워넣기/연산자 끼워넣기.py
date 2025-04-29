import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
def backTracking(depth):
    if depth == N-1:
        global minN, maxN

        ans = n_list[0]
        for i in range(1, N):
            if s[i-1] == 0:
                ans += n_list[i]
            elif s[i-1] == 1:
                ans -= n_list[i]
            elif s[i-1] == 2:
                ans *= n_list[i]
            elif s[i-1] == 3:
                if ans * n_list[i] < 0:
                    ans = abs(ans) // abs(n_list[i])
                    ans = ans*-1
                else:
                    ans = ans // n_list[i]
                    
        if maxN < ans:
            maxN = ans
        if minN > ans:
            minN = ans
        return


    for i in range(4):
        if ex_list[i] != 0:
            s.append(i)
            ex_list[i] -= 1
            backTracking(depth+1)
            s.pop(-1)
            ex_list[i] += 1


N = int(input())
n_list = list(map(int, input().split()))
s = []
ex_list = list(map(int, input().split()))

minN = 100000000000
maxN = -100000000000
backTracking(0)
print(maxN)
print(minN)
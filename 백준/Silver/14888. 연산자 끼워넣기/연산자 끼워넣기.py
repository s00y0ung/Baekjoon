import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
def backTracking(s, depth):
    if depth == N:
        global minN, maxN

        if maxN < s:
            maxN = s
        if minN > s:
            minN = s
        return

    if ex_list[0] != 0:
        ex_list[0] -= 1
        backTracking(s+n_list[depth], depth+1)
        ex_list[0] += 1

    if ex_list[1] != 0:
        ex_list[1] -= 1
        backTracking(s-n_list[depth], depth+1)
        ex_list[1] += 1

    if ex_list[2] != 0:
        ex_list[2] -= 1
        backTracking(s*n_list[depth], depth+1)
        ex_list[2] += 1

    if ex_list[3] != 0:
        ex_list[3] -= 1
        tmp = s // n_list[depth]
        if s * n_list[depth] < 0:
            tmp = abs(s) // abs(n_list[depth])
            tmp *= -1
        backTracking(tmp, depth+1)
        ex_list[3] += 1


N = int(input())
n_list = list(map(int, input().split()))
ex_list = list(map(int, input().split()))

minN = 100000000000
maxN = -100000000000

s = n_list[0]
backTracking(s,1)

print(maxN)
print(minN)
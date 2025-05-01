import sys
input = sys.stdin.readline

S = input().rstrip()
N = int(input())
prefix = [[0 for _ in range(26)] for _ in range(len(S)+1)]

for idx in range(1,len(S)+1):
    t = ord(S[idx-1]) - 97
    for j in range(26):
        if j == t:
            prefix[idx][t] = prefix[idx-1][t] + 1
        else:
            prefix[idx][j] = prefix[idx-1][j]

for _ in range(N):
    alpha, l, r = input().split()
    alpha = ord(alpha) - 97

    print(prefix[int(r)+1][alpha] - prefix[int(l)][alpha])
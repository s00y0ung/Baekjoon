import sys
input = sys.stdin.readline

S = input().rstrip()
N = int(input())
prefix = [[0] * 26]

for idx in S:
    p = list(prefix[-1])
    p[ord(idx)-97] += 1
    prefix.append(p)

for _ in range(N):
    alpha, l, r = input().split()
    alpha = ord(alpha) - 97

    print(prefix[int(r)+1][alpha] - prefix[int(l)][alpha])
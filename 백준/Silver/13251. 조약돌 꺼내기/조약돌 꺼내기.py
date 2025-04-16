import sys
import math
input = sys.stdin.readline


M = int(input()) # 조약돌 색상
N_list = list(map(int, input().split())) # 조약돌 개수
K = int(input()) # K 개수

total = sum(N_list)
t = 0
for n in N_list:
    t += math.comb(n, K)
print(t / math.comb(total, K))
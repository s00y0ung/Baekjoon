import sys
input = sys.stdin.readline

def factorial(a):
    ans = 1
    for idx in range(1, a+1):
        ans = ans * idx
    return ans

def get_c(n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))

M = int(input()) # 조약돌 색상
N_list = list(map(int, input().split())) # 조약돌 개수
K = int(input()) # K 개수

total = sum(N_list)
t = 0
for idx in N_list:
    t += get_c(idx, K)
print(t/get_c(total, K))
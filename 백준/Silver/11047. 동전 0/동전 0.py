import sys
input = sys.stdin.readline

N, K = map(int, input().split())
value = []
for i in range(N):
    value.append(int(input()))

cnt = 0
for coin in range(N-1, -1, -1):
    if K >= value[coin]:
        cnt += K//value[coin]
        K = K % value[coin]
    if K == 0:
        break
print(cnt)

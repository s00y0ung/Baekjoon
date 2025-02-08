import sys
input = sys.stdin.readline

N, H = map(int, input().split())

bottom_list = [0 for i in range(H + 1)]
bottom_prefix_sum = [0 for i in range(H + 2)]
top_list = [0 for i in range(H + 1)]
top_prefix_sum = [0 for i in range(H + 2)]
obstacle = [0 for i in range(H+1)]

for i in range(int(N/2)):
    n = int(input())
    bottom_list[n] += 1

    n = int(input())
    top_list[n] += 1


for i in range(H,0,-1):
    bottom_prefix_sum[i] += (bottom_prefix_sum[i+1] + bottom_list[i])
    top_prefix_sum[i] += (top_prefix_sum[i+1] + top_list[i])

for i in range(1,H+1):
    obstacle[i] = bottom_prefix_sum[i] + top_prefix_sum[H-i+1]


del obstacle[0]
minNum = min(obstacle)
print(minNum, obstacle.count(minNum))
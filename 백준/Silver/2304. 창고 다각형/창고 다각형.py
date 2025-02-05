N = int(input())
area_arr = [0 for i in range(1001)]
start_s = 1001
end_s = 0
maxNum = 0
maxIdx = 0

for i in range(N):
    L, H = map(int, input().split())
    area_arr[L] = H

    if start_s > L: start_s = L
    if end_s < L: end_s = L
    if maxNum < H:
        maxNum = H
        maxIdx = L

front_a = area_arr[start_s:maxIdx]
rear_a = area_arr[maxIdx+1:end_s+1]
area = maxNum
stick = 0
for a in front_a:
    if a > stick:
        stick = a
    area += stick
stick = 0
for a in rear_a[::-1]:
    if a > stick:
         stick = a
    area += stick
print(area)
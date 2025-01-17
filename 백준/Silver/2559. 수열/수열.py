N, K = map(int, input().split())
temp = list(map(int, input().split()))
temp_prefix = [0]
count = 0

for t in temp:
    count += t
    temp_prefix.append(count)
temp_max = -10000000
for i in range(K, N+1):
    count = temp_prefix[i] - temp_prefix[i-K]
    if count > temp_max:
        temp_max = count

print(temp_max)
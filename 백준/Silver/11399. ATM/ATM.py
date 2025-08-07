n = int(input())
time = list(map(int, input().split()))
time.sort(reverse = True)

answer = 0
for i in range(n):
    answer += (i+1)*time[i]
print(answer)
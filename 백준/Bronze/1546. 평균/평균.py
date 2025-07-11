n = int(input())
num = list(map(int, input().split()))
m = max(num)

for i in range(n):
    num[i] = (num[i]/m*100)
ans = sum(num) / n
print(ans)
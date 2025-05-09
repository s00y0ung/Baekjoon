N = int(input())
F = int(input())

if N > 100:
    N = (N // 100) * 100

ans = 0
while (N+ans) % F != 0:
    ans += 1
print(f'{ans:02}')
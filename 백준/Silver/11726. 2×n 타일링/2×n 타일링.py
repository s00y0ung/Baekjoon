N = int(input())

stick = [1 for _ in range(N+1)]
stick[1] = 1
for idx in range(2, N+1):
    stick[idx] = (stick[idx-1] + stick[idx-2]) % 10007
print(stick[N])
N = int(input())
num_list = list(map(int, input().split()))
line = [0 for _ in range(N)]

for i in range(N):
    tmp = num_list[i]
    t = 0

    for j in range(N):
        if line[j] == 0:
            if t == tmp:
                line[j] = i+1
                break
            t += 1
print(*line)
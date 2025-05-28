N, L ,D = map(int, input().split())
time = 0
for t in range(N):
    time += L
    for i in range(1,5):
        if time % D == 0:
            break
        time += 1

    if time % D == 0:
        break
    time += 1

if time % D != 0:
    while time % D != 0:
        time += 1
print(time)
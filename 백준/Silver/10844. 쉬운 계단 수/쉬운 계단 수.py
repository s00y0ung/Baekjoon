N = int(input())
stick =[[0 for _ in range(10)] for _ in range(N+1)]
stick[1] = [0,1,1,1,1,1,1,1,1,1]
for idx in range(2,N+1):
    stick[idx][0] = stick[idx-1][1]
    stick[idx][9] = stick[idx-1][8]
    for i in range(1, 9):
        stick[idx][i] = (stick[idx-1][i-1] + stick[idx-1][i+1]) % 1000000000
print(sum(stick[N]) % 1000000000)
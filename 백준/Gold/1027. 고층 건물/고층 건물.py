N = int(input())
buildings = list(map(int,input().split()))
see = [0 for i in range(N)]

for i in range(N-1):
    slope = -10000000000
    for j in range(i+1, N):
        if slope < ((buildings[j]-buildings[i])/(j-i)):
            slope = ((buildings[j]-buildings[i])/(j-i))
            see[i] += 1

for i in range(N-1,0,-1):
    slope = 10000000000
    for j in range(i-1,-1,-1):
        if slope > ((buildings[i]-buildings[j])/(i-j)):
            slope = ((buildings[i]-buildings[j])/(i-j))
            see[i] += 1
print(max(see))
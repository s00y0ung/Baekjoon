N = int(input())

ans = 1
p1,p2 = 1,2
end = N //2
total = p1+p2
while p1 < p2 <= end+1:
    if total == N:
        ans += 1
        p2 += 1
        total = total - p1 + p2
        p1+=1


    elif total > N:
        total -= p1
        p1 += 1
    else: # total < N:
        p2 += 1
        total += p2

print(ans)
N = int(input())
dice = [*map(int, input().split())]

one_face = min(dice)
two_face = 10000
three_face = 10000

for i in range(6):
    for j in range(6):
        if i + j == 5 or i == j: # A-F , B-E, C-D
            continue
        if two_face > dice[i] + dice[j]:
            two_face = dice[i] + dice[j]

t_face =[[0,1,2],[0,1,3],[0,2,4],[0,3,4],[1,2,5],[1,3,5],[2,4,5],[3,4,5]]
for t1,t2,t3 in t_face:
    if three_face > dice[t1] + dice[t2] + dice[t3]:
        three_face = dice[t1] + dice[t2] + dice[t3]
ans = 0
if N == 1:
    ans = sum(dice) - max(dice)
elif N != 0:
    ans += three_face * 4
    ans += (two_face * (4 * (2*N - 3)))
    ans += (one_face * ((N - 2) * (N - 2) + (N - 2) * (N - 1) * 4))
print(ans)
def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return # x와 y가 같은 집합에 있을 경우

    if people[x_root] < people[y_root]:
        people[x_root] += people[y_root]
        people[y_root] = x_root
    else:
        people[y_root] += people[x_root]
        people[x_root] = y_root

def find(x):
    if people[x] < 0:
        return x
    return find(people[x])


N, M = map(int, input().split())
people = [-1 for i in range(N+1)]
truth = list(map(int, input().split()))
for tidx in truth[2:]:
    union(truth[1], tidx)

party = [[] for _ in range(M)]
for p in range(M):
    party[p] = list(map(int, input().split()))
    for pidx in party[p][2:]:
        union(party[p][1], pidx)

ans = M
if truth[0] != 0:
    truth_root = find(truth[1])

    for p_list in party:
        for p in p_list[1:]:
            if find(p) == truth_root:
                ans -= 1
                break;

print(ans)
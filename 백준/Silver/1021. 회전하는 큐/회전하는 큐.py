m,n = map(int, input().split())
n_list = list(map(int, input().split()))

queue = [i for i in range(1, m+1)]
size = m

p = 0
leftp = 0
rightp = 0
ans = 0
for n in n_list:
    leftp, rightp = 0, p
    while queue[p] != n:
        p = p-1
        if p < 0:
            p += size
        leftp += 1


    p, rightp = rightp, 0
    while queue[p] != n:
        p = (p + 1) % size
        rightp += 1

    if leftp < rightp:
        ans += leftp
        queue.pop(p)
    else:
        ans += rightp
        queue.pop(p)
    size -= 1
    if size > 0:
        p = p % size
print(ans)
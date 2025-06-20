def solution(cap, n, deliveries, pickups):
    answer = 0
    prefix_d = [deliveries[-1]]
    prefix_p = [pickups[-1]]

    for i in range(n-2,-1,-1):
        prefix_d.append(prefix_d[-1] + deliveries[i])
        prefix_p.append(prefix_p[-1] + pickups[i])

    d,p = 0,0
    while d < n and prefix_d[d] == 0:
        d += 1
    while p < n and prefix_p[p] == 0:
        p += 1
            
    cnt = 1
    c = cap
    while d < n or p < n:

        answer += max(n - d, n - p)
        while d < n and prefix_d[d] <= c:
            d += 1
        while p < n and prefix_p[p] <= c:
            p += 1

        cnt += 1
        c = cap * cnt

    return answer * 2
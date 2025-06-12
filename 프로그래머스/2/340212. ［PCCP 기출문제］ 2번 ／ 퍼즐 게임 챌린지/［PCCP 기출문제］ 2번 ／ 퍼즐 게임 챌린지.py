def time_limit(m, diffs, times):

    cnt = 0
    for i in range(len(diffs)):
        if diffs[i] <= m:
            cnt += times[i]
        else:
            t = diffs[i]-m
            cnt += ((t+1)*times[i])
            cnt += (t*times[i-1])
    return cnt

def solution(diffs, times, limit):
    left = 1
    right = max(diffs)

    while left <= right:
        mid = (left + right) // 2
        t = time_limit(mid, diffs, times)
        print(mid,t)
        if t > limit:
            left = mid+1
        else:
            right = mid-1
    return left
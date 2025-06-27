def solution(n):
    answer = 0
    q = []
    for i in range(1,n+1):
        q.append(i)
        if sum(q) < n:
            continue

        while sum(q) > n:
            q.pop(0)
        if sum(q) == n:
            print(q)
            answer += 1
    return answer
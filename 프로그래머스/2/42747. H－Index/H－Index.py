def solution(citations):
    answer = 0

    citations.sort(reverse = True)
    print(citations)

    for h in range(max(citations),-1,-1):
        above = len([c for c in citations if c >= h])
        under = len([c for c in citations if c <= h])
        if under <= h <= above:
            return h
    return answer
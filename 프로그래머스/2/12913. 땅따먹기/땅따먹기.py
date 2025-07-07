def solution(land):
    for l in range(1,len(land)):
        for i in range(4):
            land[l][i] += max([land[l-1][k] for k in range(4) if i != k])

    return max(land[len(land)-1])
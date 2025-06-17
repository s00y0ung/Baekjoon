def solution(storey):
    answer = 0

    while storey:
        s = storey % 10
        storey = storey // 10
        if s > 5:
            answer += (10 - s)
            storey += 1
        elif s == 5 and storey%10 >= 5:
            answer += (10-s)
            storey += 1
        else:
            answer += (s)

    return answer
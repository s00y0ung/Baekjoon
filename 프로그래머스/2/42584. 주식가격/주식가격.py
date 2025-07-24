def solution(prices):
    answer = [0 for _ in range(len(prices))]

    for p in range(len(prices)-1,-1,-1):
        cnt = 0
        for i in range(p+1, len(prices)):
            if prices[p] <= prices[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer[p] = cnt
    return answer
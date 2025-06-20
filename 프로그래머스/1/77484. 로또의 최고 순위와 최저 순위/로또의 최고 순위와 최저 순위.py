def solution(lottos, win_nums):
    cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
    zero = lottos.count(0)
    answer = [min(7-(cnt+zero),6), min(7-cnt, 6)]
    return answer
from itertools import combinations

def solution(n, q, ans):
    answer =0
    all_comb = list(combinations(range(1, n+1),5))
    for comb in all_comb:
        cnt = 0

        for k in range(len(ans)):
            cnt = 0
            for idx in range(5):
                if q[k][idx] in comb:
                    cnt += 1
            if cnt != ans[k]:
                cnt = -1
                break
        if cnt != -1:
            answer += 1

    return answer
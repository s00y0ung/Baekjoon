from collections import Counter
def solution(k, tangerine):
    answer = 0
    t_dic = Counter(tangerine)
            
    sort_t_dic = sorted(t_dic.items(), key = lambda x : -x[1])
    cnt = 0
    for st in sort_t_dic:
        if cnt >= k:
            break
        cnt += st[1]
        answer += 1
    
    return answer
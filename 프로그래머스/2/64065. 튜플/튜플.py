from collections import Counter
def solution(s):
    s = s.replace('{',"")
    s = s.replace('}',"")
    s = s.split(',')
    
    t = Counter(s)
    t = sorted(t.items(), key = lambda x : -x[1])
    answer = []
    for a in t:
        answer.append(int(a[0]))
    return answer
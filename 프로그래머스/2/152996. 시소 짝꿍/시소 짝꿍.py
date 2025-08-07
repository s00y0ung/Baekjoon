from collections import Counter

def get_balance(a,b):
    if a*2 == b*3: return 1
    if a*2 == b*4: return 1
    if a*3 == b*2: return 1
    if a*3 == b*4: return 1
    if a*4 == b*2: return 1
    if a*4 == b*3: return 1
    return 0

def solution(weights):
    answer = 0
    count_w = list(Counter(weights).items())
    for c in range(len(count_w)):
        answer = answer + (count_w[c][1]*(count_w[c][1]-1)//2)
        for i in range(c+1, len(count_w)):
            b = get_balance(count_w[c][0], count_w[i][0])
            answer += b*count_w[c][1]*count_w[i][1]
    
    return answer
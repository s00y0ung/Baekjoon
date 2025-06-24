def solution(answers):
    answer = []
    f = [1,2,3,4,5]
    s = [2,1,2,3,2,4,2,5]
    t = [3,3,1,1,2,2,4,4,5,5]
    
    correct = [0,0,0]
    cnt = 0
    for a in answers:
        if a == f[(cnt % 5)]: correct[0] += 1
        if a == s[(cnt % 8)]: correct[1] += 1
        if a == t[(cnt % 10)]: correct[2] += 1
        cnt += 1 
        
    m = max(correct)
    for i in range(3):
        if correct[i] == m:
            answer.append(i+1)
            
    return answer
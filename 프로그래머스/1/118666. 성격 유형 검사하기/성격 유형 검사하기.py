def solution(survey, choices):
    answer = ''
    type = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for idx in range(len(choices)):
        if choices[idx] > 4:
            type[survey[idx][1]] += (choices[idx]-4)    
        else:
            type[survey[idx][0]] += (4-choices[idx])
    
    key = list(type.keys())
    for idx in range(0,8,2):
        if type[key[idx]] < type[key[idx+1]]:
            answer += key[idx+1]
        else:
            answer += key[idx]
        
    
    return answer
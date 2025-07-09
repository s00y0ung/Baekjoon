def solution(progresses, speeds):
    answer = []
    while progresses:
        r = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            r+=1
        if r:
            answer.append(r)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
    return answer
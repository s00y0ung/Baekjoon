def solution(progresses, speeds):
    answer = []
    cnt = 0
    for i in range(len(progresses)):
        
        time = (100 - progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]:
            time += 1
        
        if cnt >= time:
            answer[-1] += 1
        else:
            cnt = time
            answer.append(1)
        
    return answer
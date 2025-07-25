def solution(sequence):
    answer = -1
    prefix = [0]
    for s in range(len(sequence)):
        prefix.append(prefix[-1] + sequence[s]*answer)
        answer *= -1
        
    return abs(max(prefix) - min(prefix))
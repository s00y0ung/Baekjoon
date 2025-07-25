def get_s(sequence):
    prefix = [0 for _ in range(len(sequence))]
    prefix[0] = sequence[0]
    for s in range(1, len(sequence)):
        prefix[s] = max(sequence[s], prefix[s-1]+sequence[s])
    return max(prefix)
    
    
def solution(sequence):
    answer = 1
    for s in range(len(sequence)):
        sequence[s] *= answer
        answer *= -1
    m1 = get_s(sequence)
    
    for s in range(len(sequence)):
        sequence[s] *= -1
    m2 = get_s(sequence)
    
    return max(m1,m2)
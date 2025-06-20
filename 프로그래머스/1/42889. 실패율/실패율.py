def solution(N, stages):
    answer = {}
    challenge = [0 for i in range(N + 1)]
    for s in stages:
        challenge[s - 1] += 1

    total = len(stages)
    for c in range(N):
        if total == 0:
            answer[c+1] = 0
        else:
            answer[c+1] = challenge[c] / total
            total -= challenge[c]

    answer = sorted(answer, key=lambda x: answer[x], reverse = True)
    return answer

def solution(s):
    cnt = 0
    answer = []
    for c in s:
        if c == ' ':
            cnt = 0
            answer.append(' ')
            continue
        if cnt % 2 == 0:
            answer.append(c.upper())
        else:
            answer.append(c.lower())
        cnt+=1
    return ''.join(answer)
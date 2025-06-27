def solution(s):
    answer = [s[0].upper()]
    prev = 0
    for c in range(1,len(s)):  
        if s[c] == ' ':
            prev = 1
            answer.append(' ')
            continue
        if prev:
            answer.append(s[c].upper())
            prev = 0
        else:
            answer.append(s[c].lower())

    return ''.join(answer)
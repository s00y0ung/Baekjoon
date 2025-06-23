def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        elif 97 <= ord(c) <= 122:
            answer += chr(ord(c)+n if ord(c)+n <= 122 else ord(c)+n-26)
        else:
            answer += chr(ord(c)+n if ord(c)+n <= 90 else ord(c)+n-26)
    return answer
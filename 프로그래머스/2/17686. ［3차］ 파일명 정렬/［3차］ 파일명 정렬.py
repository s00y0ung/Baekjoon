def solution(files):
    answer = []
    cnt = 0
    for f in files:
        si,ei = 0,0
        while 48 > ord(f[si]) or ord(f[si]) > 57:
            si += 1
        ei = si
        while 48 <= ord(f[ei]) <= 57:
            ei += 1
            if ei >= len(f):
                ei = 0
                break
        if ei == 0:
            answer.append([f[:si], f[si:],"",cnt])
        else:
            answer.append([f[:si], f[si:ei], f[ei:], cnt])
        cnt += 1
         
    answer = sorted(answer, key = lambda x : (x[0].upper(),int(x[1]), x[3]))
    for a in range(len(answer)):
        answer[a] = ''.join(answer[a][:3])
    return answer
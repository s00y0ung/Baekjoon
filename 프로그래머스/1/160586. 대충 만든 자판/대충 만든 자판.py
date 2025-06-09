def solution(keymap, targets):
    answer = []
    alphas = [0 for _ in range(26)]
    
    for a in range(26):
        ks = [1000]
        for key in keymap:
            k = key.find(chr(a+65))
            if k != -1:
                ks.append(k+1)
        alphas[a] = min(ks)
        
    for target in targets:
        r = 0
        for t in target:
            if alphas[ord(t)-65] == 1000:
                r = -1
                break                
            r += alphas[ord(t)-65]
        answer.append(r)
        
    return answer
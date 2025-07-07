def solution(n, words):
    cnt = 1 # 차례
    no = 0 # 번호
    prev = words[0]
    w_repeat = [prev]
    for w in words[1:]:
        no = (no+1) % n
        if no == 0:
            cnt += 1
        if w[0] != prev[-1] or w in w_repeat:
            return [no+1,cnt]
        prev = w
        w_repeat.append(w)
        
    return [0,0]
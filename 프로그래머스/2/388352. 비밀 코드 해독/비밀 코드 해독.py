def secret(key, ans,q):
    for k in range(len(q)):
        cnt = 0
        for num in q[k]:
            if num in key:
                cnt += 1
        if cnt != ans[k]:
            return -1
    return 1

def bt(n, size, q, ans, key, s, answer):
    if size == 5:
        if secret(key, ans, q) == 1:
            answer += 1
        return answer

    for i in range(s,n+1):
        if i in key:
            continue
        key.append(i)
        answer = bt(n, size+1,q, ans, key,i+1, answer)
        key.pop(-1)

    return answer

def solution(n, q, ans):
    answer = bt(n,0, q,ans, [],1,0)
    return answer


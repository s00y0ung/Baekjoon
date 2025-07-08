def solution(want, number, discount):
    answer = 1
    w_dic = {}
    for w in range(len(number)):
        w_dic[want[w]] = number[w]

    d_dic = {}
    for d in range(10):
        if discount[d] in d_dic:
            d_dic[discount[d]] += 1
        else:
            d_dic[discount[d]] = 1
    for w in want:
        if w not in d_dic:
            answer -= 1
            break
        if w_dic[w] > d_dic[w]:
            answer -= 1
            break

    cnt = 0
    print(answer)
    for d in range(10, len(discount)):
        d_dic[discount[cnt]] -= 1
        if discount[d] in d_dic:
            d_dic[discount[d]] += 1
        else:
            d_dic[discount[d]] = 1

        answer += 1
        for w in want:
            if w not in d_dic:
                answer -= 1
                break
            if w_dic[w] > d_dic[w]:
                answer -= 1
                break
        cnt += 1

    return answer
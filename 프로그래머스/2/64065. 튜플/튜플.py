def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
# from collections import Counter
# def solution(s):
#     s = s.split('{,}')
#     print(s)
#     t = Counter(s)
#     t = sorted(t.items(), key = lambda x : -x[1])
#     answer = []
#     for a in t:
#         answer.append(int(a[0]))
#     return answer
def solution(data, ext, val_ext, sort_by):
    answer = []

    discriminate = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    idx = discriminate[ext]
    for i in range(len(data)):
        if data[i][idx] < val_ext:
            answer.append(data[i])
    answer.sort(key = lambda x : x[discriminate[sort_by]])
    return answer
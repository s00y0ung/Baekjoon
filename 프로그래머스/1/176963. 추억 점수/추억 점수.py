def solution(name, yearning, photo):
    answer = []
    people = {}
    for i in range(len(name)):
        people[name[i]] = yearning[i]

    for p_list in photo:
        result = 0
        for p in p_list:
            if p in people:
                result += people[p]
        answer.append(result)
    return answer
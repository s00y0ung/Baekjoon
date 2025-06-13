def solution(sequence, k):
    answer = []

    s, e = 0, 0
    result = sequence[0]
    while e < len(sequence) and s < len(sequence):

        if result == k:
            answer.append([s, e])
            result -= sequence[s]
            s += 1
            e += 1
            if e >= len(sequence):
                break
            result += sequence[e]

        elif result > k:
            result -= sequence[s]
            s += 1
        else:
            e += 1
            if e >= len(sequence):
                break
            result += sequence[e]

    answer.sort(key=lambda x: (-(x[0] - x[1]), x[0]))

    return answer[0]
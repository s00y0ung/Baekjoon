def solution(n, left, right):
    answer = []
    if left//n == right//n:
        for i in range(left%n, right%n+1):
            if i < left//n:
                answer.append(left//n+1)
            else:
                answer.append(i+1)
        return answer
            
    for j in range(left % n, n):
        if j < left // n:
            answer.append(left // n + 1)
        else:
            answer.append(j + 1)

    for i in range(left // n + 1, right // n):
        for j in range(n):
            if i > j:
                answer.append(i + 1)
            else:
                answer.append(j + 1)

    for j in range(right % n + 1):
        if j < right // n:
            answer.append(right // n + 1)
        else:
            answer.append(j + 1)
    return answer
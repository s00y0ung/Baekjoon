def solution(numbers):
    answer = [-1 for i in range(len(numbers))]

    for n in range(len(numbers) - 2, -1, -1):
        if numbers[n] < numbers[n + 1]:
            answer[n] = numbers[n + 1]
        elif numbers[n] == numbers[n + 1]:
            answer[n] = answer[n + 1]
        else:
            a = -1
            for k in range(n + 1, len(numbers)):
                if numbers[k] >= numbers[n]:
                    if numbers[k] == numbers[n]:
                        a = answer[k]
                    else:
                        a = numbers[k]
                    break
                
                if numbers[k] < numbers[n] and answer[k] == -1:
                    a = -1
                    break
            answer[n] = a

    return answer
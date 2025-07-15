def bt(numbers, target, total, stack, start, answer):
    a = total
    for i in stack:
        a = a - 2 * (numbers[i])
    if a == target:
        answer += 1

    for i in range(start, len(numbers)):
        stack.append(i)
        answer = bt(numbers, target, total, stack, i + 1, answer)
        stack.pop(-1)
    return answer

def solution(numbers, target):
    answer = bt(numbers, target, sum(numbers), [], 0, 0)
    return answer
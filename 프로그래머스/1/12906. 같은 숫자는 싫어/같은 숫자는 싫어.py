def solution(arr):
    answer = [arr[0]]
    prev = arr[0]
    
    for a in arr:
        if prev == a:
            continue
        prev = a
        answer.append(a)
    
    return answer
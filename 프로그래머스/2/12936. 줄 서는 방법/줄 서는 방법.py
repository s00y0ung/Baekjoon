def solution(n,k):
    answer = []
    n_list = [i for i in range(1, n+1)]
    k = k-1
    while n > 1:
        f = 1
        for i in range(1, n):
            f = f * i
        a = k // f

        answer.append(n_list[a])
        n_list.pop(a)
        k = k%(f)
        n = n-1
        
    answer.append(n_list[0])

    return answer
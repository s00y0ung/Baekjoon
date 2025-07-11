from math import factorial

def solution(n,k):
    answer = []
    n_list = [i for i in range(1, n+1)]
    k = k-1

    while n > 0:
        f = factorial(n-1)

        answer.append(n_list[k // f])
        n_list.pop(k // f)
        k = k % f

        n = n-1

    return answer
from itertools import combinations

def solution(nums):
    answer = 0
    
    prime = [1 for _ in range(3001)]
    for i in range(2,3001):
        if prime[i] == 0:
            continue
        for j in range(i+i, 3001, i):
            prime[j] = 0
         
    for c in combinations(nums, 3):
        if prime[sum(c)] == 1:
            answer += 1

    return answer
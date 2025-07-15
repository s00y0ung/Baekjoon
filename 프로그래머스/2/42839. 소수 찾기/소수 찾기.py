from itertools import permutations

def solution(numbers):
    answer = 0
    n_set = set()
    for n in range(1, len(numbers) + 1):
        for c in permutations(numbers, n):
            num = int(''.join(c))
            n_set.add(num)

    prime = [1,1] + [0 for _ in range(max(n_set))]
    for i in range(2, int(len(prime) ** 0.5) + 1):
        if prime[i] == 1:
            continue
        for j in range(i + i, len(prime), i):
            prime[j] = 1

    for s in n_set:
        if prime[s] == 0:
            answer += 1

    return answer
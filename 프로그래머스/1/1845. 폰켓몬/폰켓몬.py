def solution(nums):
    n_set = set(nums)
    return len(nums)//2 if len(n_set) > len(nums)//2 else len(n_set)
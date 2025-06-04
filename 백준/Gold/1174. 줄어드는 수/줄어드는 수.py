from itertools import combinations

N = int(input())
comb = [0,1,2,3,4,5,6,7,8,9]
nums = [0,1,2,3,4,5,6,7,8,9]
for digit in range(2,11):
    for c in combinations(comb, digit):
        nums.append(int(''.join(map(str, sorted(c, reverse = True)))))

if len(nums) < N:
    print(-1)
else:
    nums.sort()
    print(nums[N-1])
